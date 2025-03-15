import sys

input = sys.stdin.readline

n = int(input())
x = 0
ans = 0
for i in range(n):
    t = int(input())
    if t < 0:
        x += t
        if x < 0:
            ans += -x
            x = 0
    else:
        x += t

print(ans)
