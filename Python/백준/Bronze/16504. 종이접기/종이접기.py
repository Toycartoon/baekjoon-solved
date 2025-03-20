n = int(input())
ans = 0
for i in range(n):
    ans += sum(list(map(int, input().split())))

print(ans)
