for n in range(1, 100):
    r = bin(n)[2:]
    if n % 6 == 0:
        r = r + '111'
    else:
        r = r + '1'
    a = int(r, 2)
    if a % 3 == 0:
        r += r + '101'
    else:
        r += '1'

