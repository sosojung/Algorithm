n, k = map(int, input().split())
female = [0] * 1000
male = [0] * 1000
for i in range(n):
    s, y = map(int, input().split())
    if s == 0:
        female[y] += 1
    else :
        male[y] += 1

for j in range(1, 7):
    if female[j] % k == 0:
        female[j] = female[j] // k
    else :
        female[j] = (female[j] // k) + 1

    if male[j] % k == 0:
        male[j] = male[j] // k
    else :
        male[j] = (male[j] // k) + 1

print(sum(female) + sum(male))