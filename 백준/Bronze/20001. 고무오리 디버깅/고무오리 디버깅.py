cnt = 0
while True:
    n = input()
    if n == "고무오리 디버깅 끝":
        break
    elif n == "문제":
        cnt += 1
    elif n == "고무오리":
        if cnt == 0:
            cnt += 2
        else:
            cnt -= 1

if cnt == 0:
    print("고무오리야 사랑해")
else:
    print("힝구")