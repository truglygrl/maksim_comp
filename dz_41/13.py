def f(a, b):
    if a > b or a == 15:
        return 0
    if a == b:
        return 1
    return f(a + 2, b) + f(a*5, b)

print(f(3, 11)*f(11, 21)*f(21, 45))