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
    a, b, c, d = map(int, input().split())

    heapq.heappush(q, (-d, -c, b, a))


ans = 0
while q:
    _d, _c, _b, _a = heapq.heappop(q)

    if not union(_b, _a):
        ans += -_c

print(ans)
