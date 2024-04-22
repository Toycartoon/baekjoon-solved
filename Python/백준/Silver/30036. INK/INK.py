i, n, k = map(int, input().split())
ink_s = input()
m = [list(input()) for _ in range(n)]
com = input()


sx, sy, si = 0, 0, 0
for y in range(n):
    for x in range(n):
        if m[y][x] == "@":
            sx, sy = x, y
            break


w = 0
for c in com:
    if c == "U" and 0 < sy < n:
        if m[sy-1][sx] == ".":
            m[sy][sx] = "."
            m[sy-1][sx] = "@"
            sy -= 1
    elif c == "D" and 0 <= sy < n-1:
        if m[sy+1][sx] == ".":
            m[sy][sx] = "."
            m[sy+1][sx] = "@"
            sy += 1
    elif c == "L" and 0 < sx < n:
        if m[sy][sx-1] == ".":
            m[sy][sx] = "."
            m[sy][sx-1] = "@"
            sx -= 1
    elif c == "R" and 0 <= sx < n-1:
        if m[sy][sx+1] == ".":
            m[sy][sx] = "."
            m[sy][sx+1] = "@"
            sx += 1
    elif c == "j":
        si += 1
    elif c == "J":
        for a in range(n):
            for b in range(n):
                if abs(sy - a) + abs(sx - b) <= si:
                    if m[a][b] not in '.@':
                        m[a][b] = ink_s[w]
        w += 1
        if w == i:
            w = 0
        si = 0

for ans in m:
    print("".join(ans))