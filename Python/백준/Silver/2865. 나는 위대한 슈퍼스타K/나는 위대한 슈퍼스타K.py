import heapq

q = []
n, m, k = map(int, input().split())
ans = [0 for _ in range(n)]

for _ in range(m):
    l = input().split()

    for x in range(0, len(l), 2):
        i, s = l[x], l[x+1]
        heapq.heappush(q, (-float(s), int(i)))


c = 0
while c < k:
    s, i = heapq.heappop(q)

    if ans[i-1] == 0:
        c += 1
        ans[i-1] = -s


print(round(sum(ans), 2))
