d = set()
def f(a, c):
    if c > 6:
        return 0
    if c == 6:
        d.add(a)
        return
    if c < 6:
        f(a + 1, c + 1)
        f(a + 4, c + 1)
        f(a * 3, c + 1)
f(7, 0)
print(len(d))