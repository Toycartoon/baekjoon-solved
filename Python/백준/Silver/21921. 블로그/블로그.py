x, n = map(int, input().split())
a = list(map(int, input().split()))

ps = []
i = 0
for v in a:
    ps.append(i)
    i += v

ps.append(i)
ans = {}

for i in range(n, x+1):
    if not ps[i]-ps[i-n] in ans:
        ans[ps[i]-ps[i-n]] = 1
    else:
        ans[ps[i]-ps[i-n]] += 1

print(max(ans.keys()) if max(ans.keys()) != 0 else "SAD")
print(ans[max(ans.keys())] if max(ans.keys()) != 0 else "")
