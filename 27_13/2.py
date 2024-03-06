f = open('27b__14mku.txt')
n = int(f.readline())
s = 0
mr = [10000000]*17
for i in range(n):
    a, b = map(int, f.readline().split())
    s += min(a, b)
    d = abs(a-b)
    mr1 = mr[:]
    for j in range(17):
        if d + mr1[j] < mr[(d + mr[j]) % 17]:
            mr[(d + mr[j]) % 17] = d + mr1[j]

    if d < mr[d % 17]:
        mr[d % 17] = d

print(s, s % 17)
print(mr)
s += mr[17 - (s % 17)]
print(s, s % 17)