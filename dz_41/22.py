d = set()
def f(a, b):
    if (a > b) or (a % 5 == 0):
        return 0
    if a == b:
        return 1
    return f(a + 4, b) + f(a + 5, b)
print(f(31, 113))