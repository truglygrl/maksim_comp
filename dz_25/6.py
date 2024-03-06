f = open('10__1n2v6.txt')
c = 0
mx = -10000000000

a = [int(i) for i in f]
sr = sum(a) / len(a)
print(a[0:3], mx)
for i in range(len(a)-2):
    t1 = [int(x) for x in a[i:i+3] if x % 14 == 0]
    t2 = [int(x) for x in a[i:i+3] if x < sr]
    if len(t1) >= 1 and len(t2) >= 1:
        c += 1
        mx = max(a[i] + a[i+1] + a[i+2], mx)
print(c, mx)