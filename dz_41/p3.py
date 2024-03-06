f = [0]*1001
for n in range(1, 1001):
    if n <= 15:
        f[n] = 2*n*n + 4*n +3
    elif n % 3 == 0:
        f[n] = f[n-1] + n**2 + 3
    else:
        f[n] = f[n-2] + n-6
c = 0
for x in f:
    t = [i in '13579' for i in str(x)]
    if all(t):
        print(x)
        c += 1

print(c)