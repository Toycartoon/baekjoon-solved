k, d = map(int, input().split())
ans = 0
while True:
    ans += 1
    d -= k
    k *= 2

    if d < k:
        break

print(ans)