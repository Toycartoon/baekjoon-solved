import sys

input = sys.stdin.readline

m = int(input())
b = {}
for i in range(m):
    c, x, *w = map(int, input().split())

    if c == 1:
        b[w[0]] = x
    elif c == 2:
        print(b[x])
