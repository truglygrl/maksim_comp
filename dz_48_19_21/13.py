from functools import lru_cache
@lru_cache(None)

def f(a, b):
    if a +b>= 50:
        return 0
    n = [f(a+2, b), f(a*3, b), f(a, b+2), f(a, b*3)]
    t = [x for x in n if x <= 0]
    if t:
        return -max(t) + 1
    return -max(n)
c = 0
for s in range(1, 40):
    for p in range(1, 40):
        if f(s, p) == -3:
            print(s, p)
            c += 1
print(c)