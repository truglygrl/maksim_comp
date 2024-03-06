def g(n):
    if n <= 1:
        return 1
    if n % 2 == 0:
        return g(n-1) + n
    return g(n-2) + n**2
print(g(80))