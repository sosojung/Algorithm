result = 0
while True:
    try:
        n, s = input().split()
        n = int(n)
        s = int(s)
        result = s // (n+1)
        print(result)
    except EOFError:
        break
        