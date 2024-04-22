n, m, k = map(int, input().split())

f = 0
for i in range(m):
    t, r = map(int, input().split())

    f += r
    if f > k:
        print(i + 1, 1)
        exit(0)

print(-1)