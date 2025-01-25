player = list(map(int, input().split()))

team1 = []
team1.append(max(player))
player.remove(max(player))


team1.append(min(player))
player.remove(min(player))

print(abs((team1[0] + team1[1]) - (player[0] + player[1])))