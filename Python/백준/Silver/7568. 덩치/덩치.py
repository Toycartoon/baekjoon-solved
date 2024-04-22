p = []
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())

    p.append((x, y))

a = []
for i in range(n):
    x = 0
    for j in range(n):
        if j == i:
            continue
        if p[i][0] < p[j][0] and p[i][1] < p[j][1]:
            x += 1
    a.append(str(x + 1))

print(" ".join(a))