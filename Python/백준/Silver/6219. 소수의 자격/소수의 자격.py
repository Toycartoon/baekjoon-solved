a, b, d = map(int, input().split())
g = [True for i in range(b+1)]
g[1] = -1

ans = 0
for i in range(2, len(g)):
    if not g[i]:
        continue

    if str(d) in str(i) and i >= a:
        ans += 1

    for j in range(i * i, len(g), i):
        g[j] = False


print(ans)
