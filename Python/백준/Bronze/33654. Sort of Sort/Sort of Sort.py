n = int(input())
a = list(map(int, input().split()))
x = -200000

ans = []
for i in a:
    if i >= x:
        ans.append(i)
        x = i

print(*ans)
