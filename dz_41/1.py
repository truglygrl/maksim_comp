def f(n):
    if n <= 0:
        return n
    if n % 2 == 0:
        return f(n // 2)*5 + n
    return f(n-3) + f(n-4)
print(f(10) + f(20) + f(15) - f(25))