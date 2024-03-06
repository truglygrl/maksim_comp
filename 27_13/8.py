f = open('27_8_B__2wamm.txt')
#f = open('27_8_A__2waml.txt')
k = 43
n = int(f.readline())
s = 0
mr = [100000000000]*k
for i in range(n):
    a, b = map(int, f.readline().split())
    s += min(a, b)
    d = abs(a - b)
    mr1 = mr[:]
    for j in range(k):
        if d + mr1[j] < mr[(d + mr[j]) % k]:
            mr[(d + mr[j]) % k] = d + mr1[j]

    mr[d % k] = min(d, mr[d % k])

print(s, s % k)
print(mr)
s += mr[k - (s % k)]
print(s, s % k)