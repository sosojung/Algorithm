n = int(input())
for i in range(n):
    a, b, x = map(int, input().split())
    print(((a * x) + (a * -1)) + b)