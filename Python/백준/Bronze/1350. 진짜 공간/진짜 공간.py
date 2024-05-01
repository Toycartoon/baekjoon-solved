from math import ceil


n = int(input())
a = list(map(int, input().split()))
c = int(input())
ans = 0

for i in a:
    if i == 0:
        continue

    ans += c * ceil(i / c)

print(ans)
