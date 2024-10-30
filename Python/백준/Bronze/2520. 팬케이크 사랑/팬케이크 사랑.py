import sys
from math import ceil, inf

input = sys.stdin.readline

for t in range(int(input())):
    _ = input()
    cm, y, ssu, ssa, f = map(int, input().split())
    cost = [0.5, 0.5, 0.25, 0.0625, 0.5625]

    b, gs, gc, w = map(int, input().split())

    batter = min(cm // cost[0], y // cost[1], ssu // cost[2], ssa // cost[3], f // cost[4])
    print(min(int(batter), b + gs // 30 + gc // 25 + w // 10))
