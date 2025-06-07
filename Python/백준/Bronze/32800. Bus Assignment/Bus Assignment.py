import sys

input = sys.stdin.readline

ans = 0
x = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    x += b - a
    ans = max(ans, x)

print(ans)
