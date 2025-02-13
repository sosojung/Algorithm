lst = []
for _ in range(10):
    a = int(input())
    if a % 42 not in lst:
        lst.append(a % 42)
print(len(lst))