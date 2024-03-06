f = open('17-205__2wtso.txt')
a = [int(i) for i in f]
mx = -1000000000000000
c = 0
for i in range(len(a)-1):
    t = [x for x in a[i:i+2] if abs(x) % 100 == 17]
    t2 = (a[i] + a[i+1]) % 2 == 0
    if (len(t) >= 1) and (t2):
        c += 1
        mx = max(mx, a[i] + a[i+1])
print(c, mx)