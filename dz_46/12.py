def f(x):
    for i in range(2, int(x **0.5) + 1):
        if x % i == 0:
            return (x // i) - i
    return 0

k = 0
for n in range(850000, 8500000000):
    if f(n) != 0:
        if f(n) % 13 == 0:
            print(n, f(n))
            k += 1
    if k == 6:
        break