from functools import lru_cache
@lru_cache(None)

def f(a, b, q2, q1, q3):
    if a > b:
        return 0
    if a == b:
        return 1
    if q1 == 1 and q2 == 1 and q3 == 1:
        return f(a + 2, b, q2, q1, 2) + f(a * 3, b, q2, q1, 3)
    else:
        return f(a + 1, b, q2, q1, 1) + f(a + 2, b, q2, q1, 2) + f(a * 3, b, q2, q1, 3)


print(f(1, 43, 0,  0, 0))