m = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
while True:
    day, month, year = map(int, input().split())

    if day == month == year == 0:
        break

    ans = 0
    is_leap = False
    if year % 4 == 0:
        is_leap = True
        if year % 100 == 0 and year % 400 != 0:
            is_leap = False

    for i in range(1, month):
        ans += m[i]
        if i == 2 and is_leap:
            ans += 1

    ans += day

    print(ans)
