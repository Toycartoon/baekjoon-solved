a, b, k = map(int, input().split())

ans = 0
for i in range(a, b+1):
    ans += str(i).count(f"{k}")

print(ans)
