import sys

input = sys.stdin.readline

n = int(input())
x = int(input())

ans = 0
for n in range(n-1):
    a = int(input())

    if a <= x:
        x = a
    else:
        ans += a - x

print(ans)
