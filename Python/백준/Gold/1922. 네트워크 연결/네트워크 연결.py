import sys
import heapq

input = sys.stdin.readline

q = []
n = int(input())
m = int(input())
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

    arr[ir] = jr
    return True


for i in range(m):
    a, b, c = map(int, input().split())

    if a == b:
        continue

    heapq.heappush(q, (c, a, b))


ans = 0
while q:
    c, a, b = heapq.heappop(q)
    r = union(a, b)
    if r:
        ans += c

print(ans)
