import sys
from math import atan2, pi

input = sys.stdin.readline

dot = []
n = int(input())
for _ in range(n):
    x, y = map(int, input().strip().split())
    d = (x ** 2 + y ** 2) ** 0.5
    dot.append((x, y, d))

dot.sort(key=lambda x: x[2], reverse=True)
max_dist = tuple(dot[0])
max_dot = []
for x, y, dist in dot:
    if dist != max_dist[2]:
        break
    max_dot.append((x, y))

max_dot.append((max_dist[0], max_dist[1]))
max_degree = 0

for i in range(1, len(max_dot)):
    rad = atan2(max_dot[i][1], max_dot[i][0]) - atan2(max_dot[i-1][1], max_dot[i-1][0])

    if rad <= 0:
        rad += 2 * pi
    degree = rad * 180 / pi

    if degree > max_degree:
        max_degree = degree

print(max_degree)
