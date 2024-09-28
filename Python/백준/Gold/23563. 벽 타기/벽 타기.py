from math import inf
import heapq
import sys

input = sys.stdin.readline

def dijkstra(_x, _y, distance):
    distance[_y][_x] = 0
    heapq.heappush(q, (0, _x, _y))

    pos = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    while q:
        dist, x, y = heapq.heappop(q)

        if distance[y][x] < dist:
            continue

        distance[y][x] = dist
        for dx, dy in pos:
            if 0 <= dx + x < w and 0 <= dy + y < h:
                cost = dist + (0 if hanbyeol[y][x] == hanbyeol[y+dy][x+dx] == 0 else 1)
                if g[dy+y][dx+x] == "#":
                    cost = inf

                if cost < distance[dy+y][dx+x]:
                    distance[dy+y][dx+x] = cost
                    heapq.heappush(q, (cost, dx+x, dy+y))

    return distance


q = []
h, w = map(int, input().split())
g = [[*input().strip()] for _ in range(h)]
hanbyeol = [[1] * w for _ in range(h)]      # 한별이 귀여어 ^p^)b

sx, sy = -1, -1
ex, ey = -1, -1
for y in range(h):
    for x in range(w):
        if g[y][x] == "S":
            sx = x
            sy = y
        if g[y][x] == "E":
            ex = x
            ey = y
        if g[y][x] == "#":
            hanbyeol[y][x] = inf
            if y != 0 and g[y-1][x] != "#":
                hanbyeol[y-1][x] = 0
            if y != h-1 and g[y+1][x] != "#":
                hanbyeol[y+1][x] = 0
            if x != 0 and g[y][x-1] != "#":
                hanbyeol[y][x-1] = 0
            if x != w-1 and g[y][x+1] != "#":
                hanbyeol[y][x+1] = 0


ans = dijkstra(sx, sy, [[inf] * w for _ in range(h)])
print(ans[ey][ex])
