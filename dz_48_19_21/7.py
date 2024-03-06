from functools import lru_cache
@lru_cache(None)

def f(a, b, c):
    if a + b + c >= 300:
        return 0
    n = [f(a + b + c, b, c), f(a*3, b, c), f(a, b+a+c, c), f(a, b*3, c), f(a, b, c+b+a), f(a, b, c*3)]
    t = [x for x in n if x <= 0]
    if t:
        return -max(t) + 1
    return -max(n)
a = []
for s in range(1, 101):
    if f(45, s, s+25) == 3:
        a.append(s)

print(a)
print(max(a), min(a))
cc = 1
for i in range(len(a)):
    cc = cc*a[i]


print(cc)