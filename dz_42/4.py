f = open('26_3__1vv31.txt')
k = int(f.readline())
n = int(f.readline())
a = sorted(list(map(int, i.split())) for i in f)
c = 0
mx = -1
for j in range(1, k+1):
    if len(a)!=0:
        t = [a[0]]
        a.pop(0)
        l = []
        for i in range(len(a)):
            if a[i][0] > t[-1][1]:
                t.append(a[i])
                l.append(i)
                mx = max(mx, t[-1][0])
        l = l[::-1]
        for i in l:
            a.pop(i)
        print(j, t)
        c += len(t)
print(c)
print(mx)