
def f(a, b):
    if a > b or a == 20:
        return 0
    if a == b:
        return 1
    return f(a + 2, b) + f(a + 6, b) + f(a*3, b)
print(f(4, 14)*f(14, 42))