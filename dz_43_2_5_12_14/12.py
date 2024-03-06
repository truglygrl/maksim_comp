def f(x):
    s = ''
    while x > 0:
        s = str(x % 3) + s
        x //= 3
    return s
for n in range(1, 100):
    r = f(n)
    if r.count('2') > 0:
        r = r + '0'
    else:
        a = f(int(str(n)[-1]) // 2)
        r += a
    if n == 5:
        print(r)
    if n == 12:
        print(r)
    if int(r, 3) > 202:
        print(int(r, 3))
        break