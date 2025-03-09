n, p = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
x = []
for i in range(n):
    x.append(p * (i + 1) - (a[i] - a[0]))

print(max(x))
