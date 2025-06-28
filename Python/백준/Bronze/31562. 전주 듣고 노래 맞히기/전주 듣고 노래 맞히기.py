n, m = map(int, input().split())
w = {}

for i in range(n):
    t, s, *a = input().split()
    if tuple(a[:3]) in w:
        w[tuple(a[:3])] = "?"
    else:
        w[tuple(a[:3])] = s

for i in range(m):
    a = tuple(input().split())

    if a in w:
        print(w[a])
    else:
        print("!")
