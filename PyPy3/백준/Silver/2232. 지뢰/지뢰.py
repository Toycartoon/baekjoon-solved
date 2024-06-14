import heapq
import sys

input = sys.stdin.readline

n = int(input())
p = [int(input()) for i in range(n)]
q = []
for i in range(n):
    heapq.heappush(q, (-p[i], i+1))

arr = [True] * n

ans = []
while arr.count(True):
    x, i = heapq.heappop(q)
    if arr[i-1]:
        ans.append(i)

    bx = -x
    ax = -x

    arr[i-1] = False
    for s in range(i-2, -1, -1):
        if arr[s] and p[s] < bx:
            bx = p[s]
            arr[s] = False
        else:
            break

    for s in range(i, n):
        if arr[s] and p[s] < ax:
            ax = p[s]
            arr[s] = False
        else:
            break


ans.sort()
for i in ans:
    print(i)
