import heapq

n, t = map(int, input().split())
ans = 0

q = []
p = [[] for _ in range(t)]
for i in range(n):
    c, x = map(int, input().split())
    p[x].append(-c)

for i in range(t-1, -1, -1):
    for x in p[i]:
        heapq.heappush(q, x)

    if len(q) > 0:
        ans -= heapq.heappop(q)

print(ans)
