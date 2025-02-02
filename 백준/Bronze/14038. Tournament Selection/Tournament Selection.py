games = []
w = 0
l = 0
for i in range(6):
    games.append(input())
for i in games :
    if i == 'W' :
        w += 1

if w >= 5 : print(1)
elif w >= 3 : print(2)
elif w >= 1 : print(3)
else : print(-1)