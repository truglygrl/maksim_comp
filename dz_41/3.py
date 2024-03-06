def f(n):
    if n == 0:
        return 6
    if n > 0:
        return 2*f(n-4)
    return 2*n + 5 + f(n)
print(f(12))