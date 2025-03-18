d1, d2, x = map(int, input().split())
if d1 < d2:
    d1, d2 = d2, d1

print(100 / ((100 - x) / d2 + (x / d1)))
