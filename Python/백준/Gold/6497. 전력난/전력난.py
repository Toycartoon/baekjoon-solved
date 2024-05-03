import sys
import heapq


input = sys.stdin.readline


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


while True:
    m, n = map(int, input().split())

    if m == n == 0:
        break

    q = []
    arr = [-1] * (m + 1)
    w = 0
    ans = 0
    for _ in range(n):
        x, y, z = map(int, input().split())

        heapq.heappush(q, (z, x, y))
        ans += z

    while q:
        x, _a, _b = heapq.heappop(q)

        r = union(_a, _b)
        if r:
            w += x

    print(ans - w)
