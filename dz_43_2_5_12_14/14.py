for n in range(1, 10000):
    r = oct(n)[2:]
    t1 = [int(x) for x in r if int(x) % 2 == 0]
    t2 = [int(x) for x in r if int(x) % 2 != 0]
    if len(t1) > len(t2):
        a = oct(sum(t1))[2:]
        r += a
    elif len(t2) > len(t1):
        a = oct(sum(t2))[2:]
        r += a
    elif len(t1) == len(t2):
        a = oct(sum(t1) // 2)[2:]
        r += a
    if int(r, 8) <= 870:
        print(n)