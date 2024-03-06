d = set()
def f(a, c):
    if c > 8:
        return 0
    if c == 8:
        d.add(a)
        return
    if c < 8:
        f(a + 5, c + 1)
        f(a - 3, c + 1)
        f(a * 4, c + 1)
f(12, 0)
print(len(d))