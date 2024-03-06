def f(x):
    s = ''
    while x > 0:
        s = str(x % 3) + s
        x //= 3
    return s



for n in range(1, 100):
    r = f(n)
    if n % 5 == 0:
        r += '02'
    else:
        a = f((n % 5)*3)
        r = r + a[-2:]
    if n == 12:
        print(r)
    if n == 5:
        print(r)
    if int(r, 3) == 192:
        print(n)
        break