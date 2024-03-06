f = open('17-324__2wtsr.txt')
a = [int(i) for i in f]
mx = -1000000000000000
c = 0
cc = ss = 0
sr = sum([x for x in a if x % 37 != 0]) / len([x for x in a if x % 37 != 0])

for i in range(len(a)-2):
    t1 = bin(sum(a[i:i+3]))[2:]
    t2 = min(a[i:i+3]) > sr
    if (t1 == t1[::-1]) and (min(a[i:i+3]) > sr):
        c += 1
        mx = max(mx, sum(a[i:i+3]))
print(c, mx)