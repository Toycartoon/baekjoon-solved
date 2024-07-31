import sys

input = sys.stdin.readline

n, m = map(int, input().split())
l = list(map(int, input().split()))

ans = 0
s = 0
for i in l:
    s += i
    s = max(0, s)

    if s >= m:
        ans += 1

print(ans)
