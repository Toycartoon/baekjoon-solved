import sys
import heapq

input = sys.stdin.readline
q = []

bag = []
n, k = map(int, input().split())
for i in range(n):
    m, v = map(int, input().split())
    heapq.heappush(q, (m, v))

for i in range(k):
    bag.append(int(input()))
bag.sort()

ans = 0
pq = []
for b in bag:
    while len(q) != 0 and b >= q[0][0]:
        weight, cost = heapq.heappop(q)
        heapq.heappush(pq, -cost)

    if len(pq) != 0:
        c = heapq.heappop(pq)
        ans -= c

print(ans)
