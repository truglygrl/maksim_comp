f = [0]*4000
for n in range(3999, 1, -1):
    if n > 3000:
        f[n] = n
    else:
        f[n] = 2+f[n+2]
print(f[40] - f[43])