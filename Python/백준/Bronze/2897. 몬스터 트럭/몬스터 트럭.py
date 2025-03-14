import sys

input = sys.stdin.readline

r, c = map(int, input().split())
w = [0, 0, 0, 0, 0]

g = [[*input()] for _ in range(r)]
for y in range(r-1):
    for x in range(c-1):
        s = [g[y][x], g[y][x+1], g[y+1][x], g[y+1][x+1]]

        if "#" in s:
            continue

        w[s.count("X")] += 1


for i in w:
    print(i)
