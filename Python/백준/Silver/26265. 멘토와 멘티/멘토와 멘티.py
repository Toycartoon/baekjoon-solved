import sys

input = sys.stdin.readline

g = []
for i in range(int(input())):
    a, b = input().strip().split()

    g.append((a, b))

g = sorted(sorted(g, key=lambda x: x[1], reverse=True), key=lambda x: x[0])
for i in g:
    print(*i)
