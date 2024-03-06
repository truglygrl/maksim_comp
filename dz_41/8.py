def f(n):
    if n <= 15:
        return n
    if n <= 25:
        return f(n-15) + n // 3
    return f(n-6)
print(f(20))