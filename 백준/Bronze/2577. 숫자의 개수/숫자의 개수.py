a = int(input())
b = int(input())
c = int(input())
abc = list(str(a*b*c))

lst = [0] * 10
for i in abc:
    lst[int(i)] += 1

for i in lst:
    print(i)