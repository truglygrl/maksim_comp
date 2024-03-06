import smtplib

for n in range(1, 100):
    r = bin(n)[2:]
    if n % 3 == 2:
        r = r + bin(r.count('0'))[2:]
    else:
        r = r + r[:2]
    if int(r, 2) > 122:
        print(n)
        break