n = int(input())
for i in range(n):
    t = input()
    t = t.upper()
    r_t = t[::-1]
    if t == r_t : print("Yes")
    else : print("No")
