n = int(input())
a = list(map(int, input().split()))

x = 1
ans = 0
for i in a:
    if x == i:
        x += 1
    else:
        ans += 1

print(ans)
