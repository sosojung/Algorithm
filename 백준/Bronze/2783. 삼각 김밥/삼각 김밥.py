x, y = map(int, input().split())
min_p = [x*(1000/y)]

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    min_p.append(x*(1000/y))

print(f"{min(min_p):.2f}")