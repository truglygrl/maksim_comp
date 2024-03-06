def f(a, b):
    if (a > b) or (a % 2 == 0):
         return 0
    if a == b:
        return 1
    if a % 3 == 0:
        return f(a + 1, b) + f(a + 2, b) + f(a * 3, b) + f(a + 3, b)
    if a % 3 == 1:
        return f(a + 1, b) + f(a + 2, b) + f(a * 3, b) + f(a + 2, b)
    if a % 3 == 2:
        return f(a + 1, b) + f(a + 2, b) + f(a * 3, b) + f(a + 1, b)
print(f(3, 77))