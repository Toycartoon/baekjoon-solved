from math import ceil

n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in a:
    ans += ceil(i / 2)

print(ans)