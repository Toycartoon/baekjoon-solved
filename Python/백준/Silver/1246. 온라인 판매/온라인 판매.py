import sys

input = sys.stdin.readline

n, m = map(int, input().split())
l = []

for i in range(m):
    l.append(int(input()))

l.sort()

mx = 0
ans = 0
for i in range(max(m - n, 0), m):
    s = l[i] * (m - i)
    if ans < s:
        ans = s
        mx = l[i]


print(mx, ans)
