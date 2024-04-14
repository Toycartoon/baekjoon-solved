n = int(input())
s = [True for _ in range(n+1)]
s[0] = False
s[1] = False

for i in range(len(s)):
    if not s[i]:
        continue
    for j in range(i * i, n + 1, i):
        s[j] = False


l = []
for i in range(len(s)):
    if s[i]:
        l.append(i)

p1, p2 = 0, 0
ans = 0
while p2 < len(l):
    x = sum(l[p1:p2])

    if x == n:
        ans += 1
        p2 += 1
    elif x < n:
        p2 += 1
    else:
        p1 += 1

if s[-1]:
    ans += 1

print(ans)
