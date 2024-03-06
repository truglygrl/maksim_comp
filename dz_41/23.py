def f(a, b):
    if (a > b) or (a == 33):
        return 0
    if a == b:
        return 1
    return f(a + 2, b) + f(a + 3, b) + f(a * 4, b)

c = 0
for i in range(50, 61):
    c += f(12, i)
print(c)