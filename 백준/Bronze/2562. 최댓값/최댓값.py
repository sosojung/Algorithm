j = []
for i in range(9):
    a = int(input())
    j.append(a)
max_j = max(j)
print(max_j)
index_max = j.index(max_j)
print(index_max+1)