f = [0]*(2*10**9+2)
for n in range(0, 2*10**+1):
    if n == 0:
        f[n] = 0
    if n % 2 == 0:
        f[n] = f[n // 10] + n % 10
    f[n] = f[n//10]

c = 0


for k in range(10**9, 2*10**9+1):
    if f[k] == 0:
        c += 1
print(c)