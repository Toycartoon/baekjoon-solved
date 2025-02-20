import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    x, y = map(int, input().split())

    if x < y and a[i] == 1:
        ans += y - x


print(ans)