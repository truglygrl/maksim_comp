def f(a, b):
    if a < b:
        return 0
    if a == b:
        return 1
    if int(a ** 0.5) == a**0.5:
        return f(a - 2, b) + f(a - 3, b) + f(int(a ** 0.5), b)
    return f(a - 2, b) + f(a - 3, b)
print(f(25, 3))