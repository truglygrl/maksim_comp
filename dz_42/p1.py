f = open('26-111.txt')
k = int(f.readline())
n = int(f.readline())
a = sorted([list(map(int, i.split())) for i in f]) #список всех заявок
for j in range(1, k+1):
    t = [a[0]]
    a.pop(0) #метод .pop() удаляет элемент из списка
    l = []
    for i in range(len(a)):#если время сдачи больше времени забирания багажа
        if a[i][0]>t[-1][1]:
            t.append(a[i])
            l.append(i)
    for i in l:
        a.pop(i)
    print(j, t)
    if t[-1][0]==998: #здесь 998 - время сдачи последнего багажа
        break