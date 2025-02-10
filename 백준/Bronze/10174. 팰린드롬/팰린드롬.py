n = int(input())
for i in range(n):
    t = input().upper()
    if t == t[::-1] : print("Yes")
    else : print("No")
