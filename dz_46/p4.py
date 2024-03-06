f = open('17-354__2wtsp.txt')
a = [int(i) for i in f]
mx = 1000000000000000
c = 0
mn = min(x for x in a if abs(x % 10) == 2)**2
for i in range(len(a)-1):
    t1 = [x for x in a[i:i+2] if x % 5 == 0]
    if (abs(abs(a[i]) % 10 - abs(a[i+1]) % 10) == 1) and len(t1) == 1