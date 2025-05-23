n, k = map(int, input().split())
s = []
for a in range(n):
    s.append(int(input()))

ps = []
i = 0
for v in s:
    ps.append(i)
    i += v

ps.append(i)
ans = 0
for i in range(k, n+1):
    ans = max(ans, ps[i]-ps[i-k])

print(ans)
