f = open('27_5_A__2walh.txt')
f = open('27_5_B__2wali.txt')
k = 23
n = int(f.readline())
s = 0
mr = [1000000000000]*k
for i in range(n):
    a, b = map(int, f.readline().split())
    s += max(a, b)
    d = abs(a - b)
    mr1 = mr[:]
    for j in range(k):
        if d + mr1[j] < mr[(d + mr[j]) % k]:
            mr[(d + mr[j]) % k] = d + mr1[j]
    mr[d % k] = min(mr[d % k], d)

print(s , s % k)
print(mr)
s -= mr[s % k]
print(s, s % k)