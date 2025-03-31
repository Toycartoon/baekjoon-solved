n, k, x = map(int, input().split())
a = list(map(int, input().split()))

ps = [0]
v = 0
for i in a:
    v += i
    ps.append(v)

l, r = 0, n
while l + 1 < r:
    mid = (l + r) // 2

    v = []
    for i in range(mid, len(ps)):
        v.append(ps[i-mid] * x + (ps[-1]-ps[i]))

    if max(v) >= k:
        l = mid
    else:
        r = mid


print(l if l > 0 else -1)
