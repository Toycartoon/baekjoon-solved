n = int(input())
k = int(input())

ans = n
for i in range(k):
    n *= 10
    ans += n

print(ans)
