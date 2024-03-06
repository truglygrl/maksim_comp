f = open('27_6_A__2walu.txt')
f = open('27_6_B__2walv.txt')
n = int(f.readline())
k = 19
mr = [1000000000000]*k
s = 0
for i in range(n):
    a, b = map(int, f.readline().split())
    s += min(a, b)
    d = abs(a - b)
    mr1 = mr[:]
    for j in range(k):
        if d + mr1[j] < mr[(d + mr[j]) % k]:
            mr[(d + mr[j]) % k] = d + mr1[j]
    mr[d % k] = min(mr[d % k], d)

print(s, s % k)
print(mr)
s += mr[k - (s % k)]
print(s, s % k)