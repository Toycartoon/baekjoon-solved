import sys

input = sys.stdin.readline

n, m = map(int, input().split())
g = [0 for _ in range(n)]
for i in range(m):
    k, s, e = map(int, input().split())

    if g[k-1] > s:
        print("NO")
    else:
        print("YES")
        g[k-1] = e
