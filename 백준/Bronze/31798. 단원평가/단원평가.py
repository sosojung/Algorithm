a, b, c = map(int, input().split())
c = c**2
if a == 0 : print(c-b)
elif b == 0 : print(c-a)
else : print(int((a+b)**0.5))
