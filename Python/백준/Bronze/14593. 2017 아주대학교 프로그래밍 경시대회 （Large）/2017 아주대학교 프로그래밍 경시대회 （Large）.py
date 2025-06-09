n = int(input())
a = []

for i in range(n):
    s, c, l = map(int, input().split())
    a.append((s, c, l, i+1))

a.sort(key=lambda x: (-x[0], x[1], x[2]))
print(a[0][-1])
