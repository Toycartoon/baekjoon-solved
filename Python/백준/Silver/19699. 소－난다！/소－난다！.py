from itertools import combinations as c

n, m = map(int, input().split())
h = list(map(int, input().split()))

s = [i for i in range(9001)]
s[1] = 0
for i in range(2, int(len(s) ** 0.5) + 1):
    if not s[i]:
        continue

    for j in range(i * i, len(s), i):
        s[j] = 0

l = set()
for i in s:
    if i:
       l.add(i)

ans = set()
for i in c(h, m):
    if sum(i) in l:
        ans.add(sum(i))

ans = sorted(list(ans))
if len(ans) == 0:
    print(-1)
else:
    print(*ans)
