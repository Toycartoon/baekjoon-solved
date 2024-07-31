n, m = map(int, input().split())

l = []
for i in range(m):
    a, b, c = input().split()
    l.append((int(a), int(b), c))

l.sort(key=lambda x: (x[1], x[0]))
for i in l:
    print(i[2], end="")
