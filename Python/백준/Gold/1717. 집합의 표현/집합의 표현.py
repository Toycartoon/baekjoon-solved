from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
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
        return

    arr[jr] = ir


for i in range(m):
    c, a, b = map(int, input().split())

    if c == 0:
        union(a, b)
    elif c == 1:
        if find(a) != find(b):
            print("NO")
        else:
            print("YES")
