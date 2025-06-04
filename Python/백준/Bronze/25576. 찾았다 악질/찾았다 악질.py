import sys

input = sys.stdin.readline

n, m = map(int, input().split())
ralpa = list(map(int, input().split()))
ans = 0

for i in range(n-1):
    v = 0

    l = list(map(int, input().split()))
    for x in range(m):
        v += abs(ralpa[x] - l[x])

    if v > 2000:
        ans += 1


if ans * 2 >= (n-1):
    print("YES")
else:
    print("NO")
