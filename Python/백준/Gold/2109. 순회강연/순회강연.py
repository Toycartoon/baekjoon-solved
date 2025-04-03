import heapq

n = int(input())
ans = 0

q = []
p = [[] for _ in range(10001)]
for i in range(n):
    x, d = map(int, input().split())
    p[d].append(-x)

for i in range(10000, 0, -1):
    for x in p[i]:
        heapq.heappush(q, x)

    if len(q) > 0:
        ans -= heapq.heappop(q)

print(ans)
