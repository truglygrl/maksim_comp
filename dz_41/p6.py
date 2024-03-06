def f(a, b, m, q15, q30):
    if a == 15:
        q15 = 1
    if a == 30:
        q30 = 1
    if a > b or a == 12 or a == 20:
        return 0
    if a == b:
        return q15*q30
    if m == 3:
        return f(a+1, b, 1, q15, q30) + f(a+2, b, 2, q15, q30)
    return f(a + 1, b, 1,q15, q30) + f(a + 2, b, 2, q15, q30) + f(a*3, b, 3, q15, q30)
print(f(2, 38, 0, 0, 0))


