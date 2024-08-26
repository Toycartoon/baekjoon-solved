x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

def ccw(a, b, c):
    return (a[0] * b[1] + b[0] * c[1] + c[0] * a[1]) - (b[0] * a[1] + c[0] * b[1] + a[0] * c[1])

print(int((ccw((x1, y1), (x2, y2), (x3, y3)) * ccw((x1, y1), (x2, y2), (x4, y4)) < 0) & (ccw((x3, y3), (x4, y4), (x1, y1)) * ccw((x3, y3), (x4, y4), (x2, y2)) < 0)))
