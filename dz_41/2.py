def f(n):
    if n >= 670:
        return n-5
    return 5*n + 7 + f(n*5 + 7)
print(f(600) - f(300))