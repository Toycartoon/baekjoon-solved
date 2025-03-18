n = int(input())
a = list(map(int, input().split()))

ans = []
for i in range(n):
    ans.append(a[i]-(n-i))

print(max(ans))
