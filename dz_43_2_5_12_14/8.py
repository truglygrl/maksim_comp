a = []
for n in range(1, 100):
    r = bin(n)[2:]
    if n % 4 == 0:
        r = r + r[-2:]
    else:
        r = r + bin((n%4)*3)[2:]
    if int(r, 2) > 76:
        a.append(int(r, 2))
print(min(a))