n, m = map(int, input().split())

x = 0
for i in range(1, n):
    if x < m:
        print(0, i)
        x += 1
    else:
        print(i-1, i)
