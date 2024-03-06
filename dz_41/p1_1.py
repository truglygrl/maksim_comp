f = [0]*100
f[0] = f[1] = 1
for n in range(2, 100):
    if n % 2 == 0:
        f[n] = n*f[n-1]
    else:
        f[n] = n+f[n-2]

print(f[84])