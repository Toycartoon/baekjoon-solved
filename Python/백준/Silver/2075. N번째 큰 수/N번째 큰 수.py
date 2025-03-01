import heapq
import sys

input = sys.stdin.readline

n = int(input())
q = []

for i in range(n):
    for x in list(map(int, input().split())):
        heapq.heappush(q, x)

    if i > 0:
        for i in range(n):
            heapq.heappop(q)

print(heapq.heappop(q))
