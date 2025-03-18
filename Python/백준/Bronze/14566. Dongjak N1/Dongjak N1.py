n = int(input())
a = list(map(int, input().split()))

a.sort()
d = {}

for i in range(1, n):
    x = a[i] - a[i-1]

    if x not in d:
        d[x] = 1
    else:
        d[x] += 1

print(min(d), d[min(d)])
