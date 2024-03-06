for n in range(1, 100):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '10' + r + '1'
    else:
        r = '1' + r + '01'
    if int(r, 2) > 420:
        print(n)