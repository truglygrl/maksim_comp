for i in range(100, 200):
    s = '1'*i
    while '111' in s:
        s = s.replace('111', '2', 1)
        s = s.replace('2222', '333', 1)
        s = s.replace('33', '1', 1)
    print(s.count('1'), i)