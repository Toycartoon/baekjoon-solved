n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
w = [5 + 2 * i for i in range(1, 101)]

visited = [False for _ in range(n+1)]
visited[0] = True

for i in a:
    visited[i] = True

if visited.count(True) == n+1:
    print(0)
    exit()

idx = []
l = -1
for i in range(1, n+1):
    if not visited[i]:
        if l == -1:
            l = i
    else:
        if l != -1:
            idx.append((l, i-1))
            l = -1

if l != -1:
    idx.append((l, n))

ans = 0
for l, r in idx:
    ans += w[r-l]

f = True
while f and len(idx) > 1:
    for i in range(1, len(idx)):
        n_idx = []
        for x in range(len(idx)):
            if x == i:
                n_idx.append((idx[i-1][0], idx[i][1]))
            elif x != i-1:
                n_idx.append(idx[x])

        v = 0
        for l, r in n_idx:
            v += w[r-l]

        if min(v, ans) == v:
            ans = v
            idx = n_idx

            f = True
            break
        else:
            f = False

print(ans)
