def f(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return i + (x // i)
    return 0

k = 0
for n in range(1567, 15670000):
    if f(n) != 0:
        if f(n) % 10 == 7:
            print(n, f(n))
            k += 1
    if k == 3:
        break