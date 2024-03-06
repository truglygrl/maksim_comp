def f(a):
    if a >= 100:
        return 0
    if a * 4 >= 120:
        n = [f(a+3)]
    else:
        n = [f(a+3), f(a*4)]
    t = [x for x in n if x <= 0]
    if t:
        return -max(t) + 1
    return -max(n)

for i in range(1, 61):
    if f(i) == 3:
        print(i, f(i))