def f(n):
    if n <= 1:
        return 0
    if n % 2 == 0:
        return f(n-1) + n // 4
    return f(n-1)*(n+1)//2 + 5
print(f(11))