t = int(input())
input()
f = sum(map(int, input().split()))

print("Padaeng_i ", end="")
print("Happy" if t <= f else "Cry")