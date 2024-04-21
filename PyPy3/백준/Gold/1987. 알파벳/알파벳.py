r, c = map(int, input().split())
g = [input() for _ in range(r)]
pos = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [[False] * c for _ in range(r)]

ans = 0

a = [0 for _ in range(26)]
hap = 0


def bt(x, y, a, visited):
    global r, c, ans, hap

    visited[y][x] = True
    a[ord(g[y][x]) - ord('A')] = 1
    hap += 1
    ans = max(ans, hap)

    for wx, wy in pos:
        if 0 <= x + wx < c and 0 <= y + wy < r:
            if not visited[y+wy][x+wx] and a[ord(g[y+wy][x+wx]) - ord('A')] == 0:
                bt(x+wx, y+wy, a, visited)

    visited[y][x] = False
    a[ord(g[y][x]) - ord('A')] = 0
    hap -= 1

    return

bt(0, 0, a, visited)
print(ans)