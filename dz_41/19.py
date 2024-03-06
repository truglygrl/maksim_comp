d = set() #создание списка
def f(a,c):
    if c > 9:
        return 0
    if c == 9:
        d.add(a)
        return
    if c < 9:
        f(a+3,c+1)
        f(a*2,c+1)
f(4,0)
print(len(d))