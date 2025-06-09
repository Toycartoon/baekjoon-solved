from datetime import datetime as dt
d, m = map(int, input().split())
print(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][dt.weekday(dt.strptime(f"2009-{m}-{d}", "%Y-%m-%d"))])
