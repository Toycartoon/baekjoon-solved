n = int(input())
l = list(map(int, input().split()))

ans = []
for i in range(n):
    ans.insert(len(ans)-l[i], i+1)

print(*ans)
