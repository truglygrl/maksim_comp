f = open('27_10_B__2wanr.txt')
#f = open('27_10_A__2wanq.txt')
n = int(f.readline())
k = 119
mr = [100000000000000000]*119
s = 0
for i in range(n):
    a, b = map(int, f.readline().split())
    s += min(a, b)
    d = abs(a-b)
    mr1 = mr[:]
    for j in range(k):
        if d + mr1[j] < mr[(d + mr[j]) % k]:
            mr[(d + mr[j]) % k] = d + mr1[j]
    mr[d % k] = min(d, mr[d % k])

print(s, s % k)
print(mr)
s += mr[k - (s % k)]
print(s, s % k)