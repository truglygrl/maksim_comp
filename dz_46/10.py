f = open('17__1vpy8.txt')
a = [int(i) for i in f]
c = 0
mx = -10000000000
for i in range(len(a)-1):
    t1 = [x for x in a[i:i+2] if (abs(x) % 9 == 0) and (abs(x) % 7 == 0) and (abs(x) % 10 == 3)]
    t2 = [x for x in a[i:i+2] if (abs(x) % 9 != 0) or (abs(x) % 7 != 0) or (abs(x) % 10 != 3)]
    if (len(t1) == 1) and (len(t2) == 1) and (t1 != t2):
        c += 1
        mx = max(mx, a[i] + a[i+1])
print(c, mx)