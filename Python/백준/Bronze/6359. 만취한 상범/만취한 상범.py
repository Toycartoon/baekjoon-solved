import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    g = [False for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(i, n+1, i):
            g[j] = not g[j]


    print(g.count(True))
