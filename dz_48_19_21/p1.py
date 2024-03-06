from functools import lru_cache
@lru_cache(None)



def f(a):
    if a >= 36:
        return 0
    if a * 3 > 85:
        n = [f(a+2)]
    else:
        n = [f(a + 2), f(a * 3)]
    t = [x for x in n if x <= 0]
    if t:
        return -max(t)+1
    return -max(n)



for i in range(1, 36):
    if f(i) == -1:
        print(i)