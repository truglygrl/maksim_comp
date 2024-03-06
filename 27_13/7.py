f = open('27_7_B__2wama.txt')
#f = open('27_7_A__2wam9.txt')
n = int(f.readline())
k = 11
mr = [100000000000]*k
s = 0
for i in range(n):
    a, b = map(int, f.readline().split())
    s += max(a, b)
    d = abs(a - b)
    mr1 = mr[:]
    for j in range(k):
        if d + mr1[j] < mr[(d + mr[j]) % k]:
            mr[(d + mr[j]) % k] = d + mr1[j]

    mr[d % k] = min(d, mr[d % k])
print(s, s % k)
print(mr)
s -= mr[s % k]
print(s, s % k)
