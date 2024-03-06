aa = []
for n in range(1, 100):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = r + '11'
    else:
        s = r.count('1')
        s = bin(s)[2:]
        r = r + s
    a = int(r, 2)
    if a > 140:
        aa.append(a)
print(min(aa))