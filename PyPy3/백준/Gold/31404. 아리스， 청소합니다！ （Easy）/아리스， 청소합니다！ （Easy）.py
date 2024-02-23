h, w = map(int, input().split())
r, c, d = map(int, input().split())
a = []
for _ in range(h):
    a.append(input())

b = []
for _ in range(h):
    b.append(input())

dust = []
for _ in range(h):
    dust.append([True] * w)


ans = 0
pos = d * 90
l = 0
while 0 <= r < h and 0 <= c < w:
    if dust[r][c]:
        dust[r][c] = False
        l = 0
        pos = (pos + int(a[r][c]) * 90) % 360
    else:
        pos = (pos + int(b[r][c]) * 90) % 360
        if l >= 16384:
            break
        l += 1

    ans += 1
    if pos == 0:
        r -= 1
    elif pos == 90:
        c += 1
    elif pos == 180:
        r += 1
    elif pos == 270:
        c -= 1


ans -= l
print(ans)
