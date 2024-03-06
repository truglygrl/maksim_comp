f = open('27PB__tcik.txt')
n = int(f.readline())
k = 4
mr = [100000000000]*k
s = 0
for i in range(n):
    a, b = map(int, f.readline().split())
    s += max(a, b)
    d = abs(a-b)
    mr1 = mr[:]
    for j in range(k):
        if d + mr1[j] < mr[(d + mr[j]) % k]:
            mr[(d + mr[j]) % k] = d + mr1[j]
    if d < mr[d % k]:
        mr[d % k] = d

print(s, s % k)
#s -= mr[s % k]
print(s, s % k)
print(mr)
