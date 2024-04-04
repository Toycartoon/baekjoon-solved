import heapq


v, e = map(int, input().split())

q = []
arr = [-1] * (v + 1)
w = 0

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


for _ in range(e):
    a, b, c = map(int, input().split())

    heapq.heappush(q, (c, a, b))


while q:
    x, _a, _b = heapq.heappop(q)

    r = union(_a, _b)
    if r:
        w += x


print(w)
