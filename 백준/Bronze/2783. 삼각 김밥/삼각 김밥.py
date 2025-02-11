x, y = map(int, input().split())
y1 = 1000 / y
x1 = x * y1

min_p = []
min_p.append(x1)

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    y_i = 1000/y
    x_i = x*y_i
    min_p.append(x_i)

print(f"{min(min_p):.2f}")
