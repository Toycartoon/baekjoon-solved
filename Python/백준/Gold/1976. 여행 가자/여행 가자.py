from sys import stdin

input = stdin.readline

n = int(input())
m = int(input())
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


for i in range(n):
    c = list(map(int, input().split()))

    for j in range(len(c)):
        if c[j] == 1:
            union(i+1, j+1)

l = list(map(int, input().split()))
f = True
u = find(l[0])
for i in l:
    if find(i) != u:
        f = False
        break

if f:
    print("YES")
else:
    print("NO")