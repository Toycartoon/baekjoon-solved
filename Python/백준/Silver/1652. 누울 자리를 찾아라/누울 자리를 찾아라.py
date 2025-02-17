import sys

input = sys.stdin.readline

n = int(input())
g = [input().strip() for _ in range(n)]

garo, sero = 0, 0
for y in range(n):
    for x in g[y].split("X"):
        if len(x) >= 2:
            garo += 1


for x in range(n):
    l = ""
    for y in range(n):
        l += g[y][x]

    for i in l.split("X"):
        if len(i) >= 2:
            sero += 1


print(garo, sero)
