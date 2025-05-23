n, m = map(int, input().split())
a = list(map(int, input().split()))

ps = []
i = 0
for v in a:
    ps.append(i)
    i += v

ps.append(i)
ans = 0

for i in range(m, n+1):
    ans = max(ans, ps[i]-ps[i-m])

print(ans)
