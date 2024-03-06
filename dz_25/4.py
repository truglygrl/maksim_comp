f = open('17__1gyan.txt')
c = 0
mx = -10000000000
a = [int(i) for i in f]
for i in range(len(a)-1):
    if (abs(a[i] - a[i+1]) % 2 == 0) and ((int(a[i] % 25 == 0) + int(a[i+1] % 25 == 0)) >= 1):
        c += 1
        mx = max(a[i] * a[i+1], mx)
print(c, mx)