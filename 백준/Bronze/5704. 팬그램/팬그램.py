while True:
    s = input()
    if s == '*':
        break
    a = [0] * 26
    for i in s:
        if i == 'a':
            a[0] += 1
        elif i == 'b':
            a[1] += 1
        elif i == 'c':
            a[2] += 1
        elif i == 'd':
            a[3] += 1
        elif i == 'e':
            a[4] += 1
        elif i == 'f':
            a[5] += 1
        elif i == 'g':
            a[6] += 1
        elif i == 'h':
            a[7] += 1
        elif i == 'i':
            a[8] += 1
        elif i == 'j':
            a[9] += 1
        elif i == 'k':
            a[10] += 1
        elif i == 'l':
            a[11] += 1
        elif i == 'm':
            a[12] += 1
        elif i == 'n':
            a[13] += 1
        elif i == 'o':
            a[14] += 1
        elif i == 'p':
            a[15] += 1
        elif i == 'q':
            a[16] += 1
        elif i == 'r':
            a[17] += 1
        elif i == 's':
            a[18] += 1
        elif i == 't':
            a[19] += 1
        elif i == 'u':
            a[20] += 1
        elif i == 'v':
            a[21] += 1
        elif i == 'w':
            a[22] += 1
        elif i == 'x':
            a[23] += 1
        elif i == 'y':
            a[24] += 1
        elif i == 'z':
            a[25] += 1
    if 0 in a:
        print("N")
    else:
        print("Y")
