from math import inf

n = int(input())
l = list(map(int, input().split()))

l.sort()

p = 0
q = n - 1
m = [inf, (0, n-1)]
while p < q:
    if abs(l[p] + l[q]) < m[0]:
        m[0] = abs(l[p] + l[q])
        m[1] = (p, q)

    if l[p] + l[q] < 0:
        p += 1
    elif l[p] + l[q] > 0:
        q -= 1
    else:
        print(l[p], l[q])
        exit()

p, q = m[1][0], m[1][1]
print(l[p], l[q])
