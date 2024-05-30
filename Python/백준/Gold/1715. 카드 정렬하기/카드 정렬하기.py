import heapq
import sys

input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    heapq.heappush(q, int(input()))


ans = 0
while q:
    try:
        x = heapq.heappop(q)
        y = heapq.heappop(q)
    except IndexError:
        break

    ans += x + y
    heapq.heappush(q, x + y)

print(ans)
