def f(x):
    s = ''
    while x > 0:
        s = str(x % 5) + s
        x //= 5
    return s
for n in range(1, 100):
    r = f(n)
    if (n % 5) % 2 == 0:
        a = f(sum(int(x) for x in r))
        r += a
    else:
        r += '21'
    if int(r, 5) <= 320:
        print(n)