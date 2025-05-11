from datetime import datetime, date

today = datetime(*map(int, input().split()))
dday = datetime(*map(int, input().split()))

ans = (dday - today).days
try:
    if date(today.year, today.month, today.day) <= date(dday.year - 1000, dday.month, dday.day):
        print("gg")
    else:
        print(f"D-{ans}")
except ValueError:
    print(f"D-{ans}")
