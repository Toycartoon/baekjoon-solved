import sys
import heapq

input = sys.stdin.readline

n = int(input())
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


for i in range(n-2):
    a, b = map(int, input().split())
    union(a, b)


ans = []
for i in range(1, n+1):
    if arr[i] == -1:
        ans.append(i)

print(*ans)
