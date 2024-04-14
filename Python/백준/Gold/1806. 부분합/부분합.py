n, s = map(int, input().split())
l = list(map(int, input().split()))

ps = []
t = 0
for i in l:
    t += i
    ps.append(t)

p1, p2 = 0, 0
ans = []
while p2 < len(l):
    x = ps[0] if p1 == 0 and p2 == 0 else ps[p2] - ps[p1]
    if x == s:
        if p2 - p1 == 0:
            ans.append(1)
        else:
            ans.append(p2 - p1)
        p2 += 1
    elif x < s:
        p2 += 1
    else:
        if p2 - p1 == 0:
            ans.append(1)
        else:
            ans.append(p2 - p1)
        p1 += 1


if ps[-1] >= s:
    ans.append(n)

if len(ans) == 0:
    ans.append(0)

print(min(ans))
