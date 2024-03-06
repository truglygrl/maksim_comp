def f(x):
    r = ''
    while x > 0:
        r = str(x % 3) + r
        x //= 3
    return r

for n in range(1, 1000):
    r = f(n)
    if n % 3 == 0:
        r = '1' + r + '02'
    else:
        r = r + f(n % 3 + 4)
    if int(r, 3) < 199:
        print(n)