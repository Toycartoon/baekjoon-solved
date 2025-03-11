import sys

input = sys.stdin.readline

n = int(input())
l = [True for _ in range(n+1)]
l[0] = False
p = [(0, 0)]
for i in range(n):
    x, y = map(int, input().split())
    p.append((x, y))

m = int(input())
dead_end = list(map(int, input().split()))
for i in dead_end:
    l[i] = False

ans = 0
for i in range(n+1):
    if l[p[i][0]] and l[p[i][1]] and l[i]:
        ans += 1

print(ans)
