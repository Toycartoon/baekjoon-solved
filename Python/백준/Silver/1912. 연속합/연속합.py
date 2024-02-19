import sys

sys.setrecursionlimit(10 ** 6)

n = int(input())
l = list(map(int, input().split()))

m = {0: l[0]}

def add(i):
    if i in m:
        return m[i]
    v1 = l[i]
    v2 = v1 + add(i - 1)
    m[i] = max(v1, v2)
    return m[i]


add(n - 1)
print(max(m.values()))
