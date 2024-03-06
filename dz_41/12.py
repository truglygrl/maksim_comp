def f(a, b):
    if a > b or a == 39:
        return 0
    if a == b:
        return 1
    return f(a + 1, b) + f(a + 10, b) + f(a*2, b)
print(f(2, 18)*f(18, 61))