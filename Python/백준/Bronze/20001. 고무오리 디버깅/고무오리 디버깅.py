q = 0
while True:
    s = input()

    if s == "고무오리 디버깅 끝":
        break

    if s == "문제":
        q += 1
    elif s == "고무오리":
        if q == 0:
            q += 2
        else:
            q -= 1

if q == 0:
    print("고무오리야 사랑해")
else:
    print("힝구")
