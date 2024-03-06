def ss(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
def f(x):
    s = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            s.add(i)
            s.add(x // i)
    return sorted(s)

c = 0
mx = -10
mn = 1000000000000000
for n in range(182635, 453734):
    t = [x for x in f(n) if ss(x)]
    if (len(t) == 2) and (t[0]*t[1] == n):
        c += 1
        mx = max(mx, n)
        mn = min(mn, n)

print(c, mx+mn)