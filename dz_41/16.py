
def f(a, b):
    if a > b or a == 31:
        return 0
    if a == b:
        return 1
    return f(a + 1, b) + f(a+5, b)
print(f(1, 21)*f(21, 66))