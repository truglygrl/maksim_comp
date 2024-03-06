from functools import lru_cache
@lru_cache(None)

def f(a, b, t, q):
    if a == 25:
        q = 1
    if a > b or a == 10 or a == 38:
        return 0
    if a == b and t <= 3 and q == 1:
        return 1
    return f(a + 1, b, t + 1, q) + f(a + 2, b, t, q) + f(a * 3, b, t, q)
print(f(1, 43, 0,0))