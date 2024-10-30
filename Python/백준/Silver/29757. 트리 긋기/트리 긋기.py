import sys

input = sys.stdin.readline

l = []
for i in range(1, int(input())+1):
    x, y = map(int, input().split())
    l.append((x, y, i))


l = sorted(sorted(l, key=lambda x: x[1]), key=lambda x: x[0])
for i in range(1, len(l)):
    print(l[i-1][2], l[i][2])
