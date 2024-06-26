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


n, m = map(int, input().split())
arr = [-1] * (n + 1)
for i in range(m):
    a, b = map(int, input().split())
    union(a, b)

ans = 0
l = list(map(int, input().split()))
for i in range(1, n):
    if find(l[i-1]) != find(l[i]):
        ans += 1

print(ans)
