a, b = [], []
n, m = map(int, input().split())

for _ in range(n):
    a.append(list(map(int, input().split())))

for _ in range(n):
    b.append(list(map(int, input().split())))

for i in range(n):
    c = []
    for j in range(m):
        c.append(str(a[i][j] + b[i][j]))
    print(" ".join(c))