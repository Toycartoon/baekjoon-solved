import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [-1 for _ in range(n)]

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


for ans in range(1, m+1):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print(ans)
        exit()
    else:
        union(a, b)

print(0)
