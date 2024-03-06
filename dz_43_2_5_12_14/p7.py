alp = '0123456789abcdefghijklm'
for x in alp:
    s1 = int('7' + x + '38596', 23)
    s2 = int('14' + x + '36', 23)
    s3 = int('61' + x + '7', 23)

    s = s1+s2+s3
    if s % 22 == 0:
        print(s // 22)