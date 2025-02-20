import sys

input = sys.stdin.readline

l = []
n, m = map(int, input().split())
for x in range(m):
    l.append(tuple(map(int, input().split())))

print(m)
for i in range(m):
    print(*l[i][:-1], end=" ")
    print(l[i-1][-1])
