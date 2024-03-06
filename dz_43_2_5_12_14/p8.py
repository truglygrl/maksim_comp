for p in range(7, 20):
    for x in range(p):
        for y in range(p):
            for z in range(p):
                s1 = y*p**2 + 3*p + y
                s2 = y*p**2 + 6*p + 5
                s3 = x*p**3 + 2*p**2 + z*p
                if s1 + s2 == s3:
                    print(x*p**2 + y*p + z)