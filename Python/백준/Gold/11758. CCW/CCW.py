x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

v1 = (x2 - x1, y2 - y1)
v2 = (x3 - x2, y3 - y2)

ccw = v1[0] * v2[1] - v1[1] * v2[0]

if ccw > 0:
    print(1)
elif ccw < 0:
    print(-1)
else:
    print(0)
