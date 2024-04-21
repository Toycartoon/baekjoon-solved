import sys
import heapq


input = sys.stdin.readline

n = int(input())
arr = [-1] * (n + 1)
w = 0

q = []
node = []
for _ in range(n):
    x, y = map(float, input().split())

    node.append((x, y))

for i in range(n):
    for j in range(n):
        if i == j:
            continue

        ix, iy = node[i]
        jx, jy = node[j]

        dist = ((ix - jx) ** 2 + (iy - jy) ** 2) ** 0.5
        heapq.heappush(q, (dist, i, j))


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

while q:
    x, a, b = heapq.heappop(q)

    r = union(a, b)
    if r:
        w += x


print(w)
