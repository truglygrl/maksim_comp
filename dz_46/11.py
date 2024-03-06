def ch(x):
    c = set()
    nc = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            if i % 2 == 0:
                c.add(i)
            else:
                nc.add(i)
            if (x // i) % 2 == 0:
                c.add(x // i)
            else:
                nc.add(x // i)
    s = nc | c
    if (len(c) == len(nc)) and (len(nc) >= 70):
        return min(x for x in s if x > 1000)
    return False



for n in range(326496, 649633):
    if ch(n) != False:
        print(n, ch(n))