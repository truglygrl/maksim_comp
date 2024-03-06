def f(x):
    s = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            s.add(i)
            s.add(x // i)
    if len(s) > 6:
        return sum(sorted(s, reverse=True)[:6])
    return 0
k = 0
for n in range(20000, 20000000):
    if f(n) > 0:
        if f(n) % 25 == 0:
            print(n, f(n))
            k +=1
    if k == 5:
        break