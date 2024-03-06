def f(x):
    d = []
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            d.append(i)
            d.append(x // i)
    return sorted(set(d))



mx = -100000000000000000
mxd = -100000000000000000
mn = -1000000000000
p = []
for n in range(3,30002):
    if len(f(n)) == 6:
        t1 = [int(x) for x in f(n) if x % 2 == 0]
        t2 = [int(x) for x in f(n) if x % 3 == 0]
        if len(t1) + len(t2) >= 6:
            p.append(n)
print(len(p))