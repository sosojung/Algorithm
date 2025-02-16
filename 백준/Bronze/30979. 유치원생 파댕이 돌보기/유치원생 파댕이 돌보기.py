t = int(input())
n = int(input())
f = []
while True:
    f = list(map(int, input().split()))
    if len(f) == n:
        break
if sum(f) >= t:
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")