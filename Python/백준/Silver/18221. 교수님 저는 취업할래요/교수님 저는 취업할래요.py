n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

gx, gy = -1, -1
sx, sy = -1, -1
for i in range(n):
    if 5 in l[i]:
        gx = l[i].index(5)
        gy = i
    if 2 in l[i]:
        sx = l[i].index(2)
        sy = i

dis = int(((gx - sx) ** 2 + (gy - sy) ** 2) ** 0.5)
student = 0
for y in range(min(gy, sy), max(gy, sy)+1):
    for x in range(min(gx, sx), max(gx, sx) + 1):
        if l[y][x] == 1:
            student += 1


print(int(student >= 3 and dis >= 5))
