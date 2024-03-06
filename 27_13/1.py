s = 0
mr = [100000]*2
f = open('27_1_B__2wafd.txt')
n = int(f.readline())
for i in range(n):
    a, b = map(int, f.readline().split())
    s += max(a, b)
    d = abs(a-b)
    mr1 = mr[:]
    for j in range(2):
        if d + mr1[j] < mr[(d + mr[j]) % 2]:
            mr[(d + mr[j]) % 2] = d + mr1[j]
    if d < mr[d % 2]:
        mr[d % 2] = d


print(s)
print(mr)
s -= mr[s % 2]
print(s)