import sys

input = sys.stdin.readline


def find(i):
    trace = []
    cur = i
    while arr[cur] != -1:
        trace.append(cur)
        cur = arr[cur]

    for v in trace:
        arr[v] = cur

    return cur


def union(i, j):
    ir = find(i)
    jr = find(j)

    if ir != jr:
        arr[ir] = jr


for t in range(int(input())):
    n = int(input())
    g = [[] for _ in range(n)]
    arr = [-1] * n

    k = int(input())
    for i in range(k):
        a, b = map(int, input().split())
        union(a, b)

    print(f"Scenario {t+1}:")
    m = int(input())
    for i in range(m):
        u, v = map(int, input().split())
        if find(u) == find(v):
            print(1)
        else:
            print(0)

    print()
