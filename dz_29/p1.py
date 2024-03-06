f = [0]*5000
for n in range(1, 3000):
    if n < 11:
        f[n] = n
    else:
        f[n] = n + f[n-1]
print(f[2024] - f[2021])