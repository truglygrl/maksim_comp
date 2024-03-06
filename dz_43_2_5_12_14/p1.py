for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if (((x <= (z == w))) or (not(y <= w))) == False:
                    print(w, x, y, z)