def f(n):
    if n > 1000:
        return n
    return 7*n*n + 3 + f(n + 1)
print(f(6) - f(12))