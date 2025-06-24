while True:
    m, a, b = map(int, input().split())

    if m == a == b == 0:
        break

    sec = round(abs((m / a) - (m / b)) * 3600)
    min = sec // 60
    sec %= 60
    hour = min // 60
    min %= 60

    print(f"{hour}:{str(min).zfill(2)}:{str(sec).zfill(2)}")
