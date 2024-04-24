import operator
from itertools import combinations as c

p = []
n = int(input())
for i in range(n):
    p.append([])
    for __ in range(5):
        p[i].append(input())

k = list(c(range(1, n + 1), 2))
a = {}
for i in range(len(k)):
    count = 0
    for y in range(5):
        for x in range(7):
            if p[k[i][0]-1][y][x] != p[k[i][1]-1][y][x]:
                count += 1

    a[k[i]] = count

l = min(a.items(), key=operator.itemgetter(1))
print(l[0][0], l[0][1])