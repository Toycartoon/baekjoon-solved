n = int(input())
a = []
for i in range(n):
    t, s = map(int, input().split())
    a.append((t, s, i+1))

a.sort(key=lambda x: (-x[1], x[0]))
print(a[0][0] + (a[0][2] - 1) * 20 if a[0][1] != 0 else 0)
