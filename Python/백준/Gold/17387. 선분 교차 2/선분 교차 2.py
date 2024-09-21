x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

def ccw(a, b, c):
    x = (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])

    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


l1 = ccw((x1, y1), (x2, y2), (x3, y3)) * ccw((x1, y1), (x2, y2), (x4, y4))
l2 = ccw((x3, y3), (x4, y4), (x1, y1)) * ccw((x3, y3), (x4, y4), (x2, y2))
is_straight = False
ans = 0

if l1 == l2 == 0:
    is_straight = True
    if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
        ans = 1

if l2 <= 0 and l1 <= 0:
    if not is_straight:
        ans = 1


print(ans)
