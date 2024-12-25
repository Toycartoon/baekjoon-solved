import sys
from itertools import permutations as p

input = sys.stdin.readline

w = list(p(["R", "S", "P"], 3))

n = int(input())
com = []
for i in range(n):
    com.append(tuple(map(int, input().split())))


ans = 0
for i in range(len(w)):
    x = 0
    for j in com:
        a, b = w[i][j[0]-1], w[i][j[1]-1]

        if (a == "R" and b == "S") or (a == "S" and b == "P") or (a == "P" and b == "R"):
            x += 1

    ans = max(ans, x)


print(ans)