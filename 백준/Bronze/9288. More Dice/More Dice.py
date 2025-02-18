for i in range(int(input())):
    x = int(input())
    print(f"Case {i+1}:")

    for a in range(1, 7):
        for b in range(a, 7):
            if a+b == x:
                print(f"({a},{b})")