n = int(input())
f = 1
for i in range(1, n+1):
    if n == 0:
        print(1)
        break
    else :
        f *= i
print(f)