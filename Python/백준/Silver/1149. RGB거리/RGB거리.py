import sys

sys.setrecursionlimit(10 ** 6)

c = []
for _ in range(int(input())):
    c.append(list(map(int, input().split())))

m = {}
def dp(f, way, cost):
    if (f, way) in m:
        return m[(f, way)]
    if f == len(c):
        return 0

    v = [0, 1, 2]
    v.remove(way)
    temp = []
    for i in v:
        temp.append(dp(f+1, i, cost) + c[f][i])

    m[(f, way)] = min(temp)
    return m[(f, way)]

l = []
for i in range(3):
    l.append(dp(0, i, c[0][i]))

print(min(l))