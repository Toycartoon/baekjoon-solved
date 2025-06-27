n, m = map(int, input().split())

w = {}
for i in range(n):
    x, v = input().split()
    w[x] = int(v)

t = 0
while t < m:
    ans = 0
    while True:
        s = input().split()

        if s == ['.']:
            break

        for i in s:
            if i in w:
                ans += w[i]

    print(ans)
    t += 1
