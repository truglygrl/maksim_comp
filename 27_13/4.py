f = open('27_4_A__2wakn.txt')
f = open('27_4_B__2wako.txt')
n = int(f.readline())
s = 0
k = 13
mr = [10000000]*k
for i in range(n):
    a, b = map(int, f.readline().split())
    s += min(a, b)
    d = abs(a-b)
    mr1 = mr[:]
    for j in range(k):
        if d + mr1[j] < mr[(d + mr[j]) % k]:
            mr[(d + mr[j]) % k] = d + mr1[j]
    mr[d % k] = min(mr[d % k], d)

print(s, s % k)
print(mr)
s += mr[k - (s % k)]
print(s, s % k)