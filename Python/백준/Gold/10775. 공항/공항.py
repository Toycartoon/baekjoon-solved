import sys


input = sys.stdin.readline

g = int(input())
p = int(input())

arr = [-1 for _ in range(g+1)]
ans = 0


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

    arr[jr] = ir

for _ in range(p):
    s = int(input())

    p = find(s)

    if p == 0:
        break


    union(p-1, p)
    ans += 1

print(ans)
