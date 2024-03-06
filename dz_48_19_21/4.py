from functools import lru_cache
@lru_cache(None)

def f(a, b, c):
    if a + b + c >= 150:
        return 0
    n = [f(a+16, b, c), f(a+32, b, c), f(a*2, b, c), f(a, b+16, c), f(a, b+32, c), f(a, b*2, c), f(a, b, c+16), f(a, b, c+32), f(a, b, c*2)]
    t = [x for x in n if x <= 0]
    if t:
        return -max(t) + 1
    return -max(n)
k = 0
for i in range(1, 67):
    if f(6, 2*i, 3*i) == -2:
        print(i)

print(k)