import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

q = []
arr = [-1] * (n + 1)


def find(i):
    trace = []
    ptr = i
    while arr[ptr] != -1:
        trace.append(ptr)
        ptr = arr[ptr]

    for v in trace:
        arr[v] = ptr

    return ptr


def union(i, j):
    ir = find(i)
    jr = find(j)

    if ir == jr:
        return False

    arr[jr] = ir
    return True


for i in range(m):
    u, v, t = map(int, input().split())
    
    heapq.heappush(q, (t, u, v))


d = 1
while q:
    w, _u, _v = heapq.heappop(q)
    if d != w or not union(_u, _v):
        break
    d += 1

print(d)
