import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
p = {}
o = {}
x = list(map(int, input().split()))
for i in range(3):
    p[x[i]] = i
    o[i] = x[i]

q = []
arr = [-1] * (n + 1)

s = 0
ans = [[0, 0], [0, 0], [0, 0]]


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
    u, v, w, k = map(int, input().split())

    heapq.heappush(q, (w, p[k], u, v))


while q:
    w, k, u, v = heapq.heappop(q)

    r = union(u, v)
    if r:
        s += w
        ans[o[k]][0] += 1
        ans[o[k]][1] += w


print(s)
for i in ans:
    print(*i)
