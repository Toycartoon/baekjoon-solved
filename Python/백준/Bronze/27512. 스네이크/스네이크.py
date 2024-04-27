n, m = map(int, input().split())

if (n * m) % 2 == 0:
    print(n * m)
else:
    print((n * m) - 1)