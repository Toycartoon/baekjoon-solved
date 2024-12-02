from math import floor, inf
from itertools import permutations as p

x, y = map(int, input().split())

l = []
for i in range(3):
    l.append(tuple(map(int, input().split())))

ans = inf
for i in list(p(range(3), 3)):
    dist = 0
    for v in range(3):
        if v == 0:
            dist += ((x - l[i[v]][0]) ** 2 + (y - l[i[v]][1]) ** 2) ** 0.5
        else:
            dist += ((l[i[v-1]][0] - l[i[v]][0]) ** 2 + (l[i[v-1]][1] - l[i[v]][1]) ** 2) ** 0.5

    ans = min(dist, ans)


print(floor(ans))
