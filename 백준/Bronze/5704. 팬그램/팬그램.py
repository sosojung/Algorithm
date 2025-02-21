a=set('abcdefghijklmnopqrstuvwxyz')
while True:
    s=input()
    if s=='*':break
    if set(s)>=a:print('Y')
    else:print('N')