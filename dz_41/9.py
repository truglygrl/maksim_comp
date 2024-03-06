def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    return f(n-1)*f(n-2) + n
print(f(2))
print(f(3))
print(f(4))
print(f(5))
print(f(6))
print(f(7))
print(f(8))