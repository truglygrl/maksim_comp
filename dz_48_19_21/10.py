from functools import lru_cache
@lru_cache(None)
def f(a):
    if a >= 65:
        return 0
    if a*3 > 109:
        n = [f(a+5), f(a+7)]
    else:
        n = [f(a+5), f(a+7), f(a*3)]
    t = [x for x in n if x <= 0]
    if t:
        return -max(t) + 1
    return -max(n)

for s in range(1, 40):
    if f(s) == 2:
        print(s)