import heapq
import sys
from math import trunc

input = sys.stdin.readline

q = []
n, h_centi, t = map(int, input().split())
for i in range(n):
    heapq.heappush(q, -int(input()))

if -min(q) < h_centi:
    print("YES\n0")
    exit()

ans = 0
while ans < t:
    x = heapq.heappop(q)
    x = trunc(x / 2) if -x != 1 else -1
    heapq.heappush(q, x)
    ans += 1

    mx = heapq.heappop(q)
    if -mx < h_centi:
        print(f"YES\n{ans}")
        exit()

    heapq.heappush(q, mx)

print(f"NO\n{-heapq.heappop(q)}")
