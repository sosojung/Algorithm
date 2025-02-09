h, m = map(int, input().split())
m = m-45
if m < 0 :
    if h-1 < 0 :
        print(24+(h-1), 60-abs(m))
    else : print(h-1, 60-abs(m))
else : print(h, m)