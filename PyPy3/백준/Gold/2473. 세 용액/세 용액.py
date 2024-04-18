from math import inf
import sys


input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

l.sort()

m = inf
ans = [0, 0, 0]
for r in range(len(l)):
    p, q = 0, n - 1

    while p < q:
        if p == r:
            p += 1
            continue
        elif q == r:
            q -= 1
            continue

        if abs(l[p] + l[q] + l[r]) < m:
            m = abs(l[p] + l[q] + l[r])
            ans = [l[p], l[q], l[r]]

        if l[p] + l[q] + l[r] == 0:
            ans = sorted([l[p], l[q], l[r]])
            print(ans[0], ans[1], ans[2])
            break
        elif l[p] + l[q] + l[r] < 0:
            p += 1
        else:
            q -= 1


ans.sort()
print(ans[0], ans[1], ans[2])
