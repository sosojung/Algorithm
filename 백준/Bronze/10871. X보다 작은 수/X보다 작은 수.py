n, x = map(int, input().split())
a = list(map(int, input().split()))
lst = []

for i in range(n):
    if a[i] < x:
        lst.append(a[i])

for i in lst:
    print(i, end=' ')