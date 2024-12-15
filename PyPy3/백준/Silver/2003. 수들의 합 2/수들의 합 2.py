from itertools import combinations as c

n, m = map(int, input().split())
a = list(map(int, input().split()))

ps = [0]
t = 0
for i in a:
    t += i
    ps.append(t)


ans = 0
for l, r in c(range(n+1), 2):
    if ps[r] - ps[l] == m:
        ans += 1


print(ans)