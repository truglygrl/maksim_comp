f = [0]*100001
f[1] = 1
for n in range(2, 100001):
    if n % 2 == 0:
        f[n] = f[n//2] + 1
    else:
        f[n] = f[n-1]+n
print(f.count(16))  