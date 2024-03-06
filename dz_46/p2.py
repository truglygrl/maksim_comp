f = open('17-1__2wtsn.txt')
a = [int(i) for i in f]
mx = -1000000000000000
sr = sum(a) / len(a)
c = 0
for i in range(len(a)-2):
    t1 = [x for x in a[i:i+3] if x < sr]
    t2 = [x for x in a[i:i+3] if '8' in str(x)]
    if len(t1) >= 1 and len(t2) >= 1:
        c += 1
        mx = max(mx, sum(a[i:i+3]))
        print(a[i:i+3])
print(c, mx)