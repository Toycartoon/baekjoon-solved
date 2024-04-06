import sys

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
        return

    arr[jr] = ir
    if p[ir] <= p[jr]:
        p[ir] += p[jr]
        p[jr] = p[ir]
    else:
        p[jr] += p[ir]
        p[ir] = p[jr]

for t in range(int(input())):
    arr = []
    p = []
    idx = {}
    i = 0
    for _ in range(int(input())):
        x, y = input().strip().split()
        if x not in idx:
            idx[x] = i
            i += 1
            arr.append(-1)
            p.append(1)
        if y not in idx:
            idx[y] = i
            i += 1
            arr.append(-1)
            p.append(1)

        union(idx[x], idx[y])
        print(abs(p[find(idx[x])]))
