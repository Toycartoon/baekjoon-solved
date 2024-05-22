from math import inf
import sys

input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
a = [0] * n

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        m = (l[max(i, j)] - l[min(i, j)]) / (max(i, j) - min(i, j))

        f = True
        for k in range(min(i, j)+1, max(i, j)):
            if l[k] - l[min(i, j)] >= m * (k - min(i, j)):
                f = False
                break

        if f:
            a[i] += 1


print(max(a))
