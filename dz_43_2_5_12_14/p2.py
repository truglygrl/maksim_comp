for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f1 = ((w <= z) == (y <= x))
                f2 = ((w <= z) and ((not x) == y))
                if int(f1)*int(f2) == 0:
                    print(w, z, y, z, int(f1), int(f2))