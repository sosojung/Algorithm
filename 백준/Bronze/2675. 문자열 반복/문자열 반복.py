t = int(input())
for i in range(t):
    r, s = input().split()
    a = int(r)
    for j in s:
        print(j * a, end="")
    print()