import sys
import heapq

input = sys.stdin.readline

q = []
n, m = map(int, input().split())
arr = [-1] * (n + 1)
w = 0
l = 0


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

for _ in range(m):
    a, b, c = map(int, input().split())

    heapq.heappush(q, (c, a, b))


while q:
    x, _a, _b = heapq.heappop(q)

    r = union(_a, _b)
    if r:
        w += x
        l = x

print(w - l)
