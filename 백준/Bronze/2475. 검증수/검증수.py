lst = list(map(int, input().split()))
sum = 0
for i in lst:
    sum += i*i
print(sum%10)