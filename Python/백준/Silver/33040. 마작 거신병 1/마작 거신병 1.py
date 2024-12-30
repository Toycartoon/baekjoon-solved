h, w = map(int, input().split())
c, d = map(int, input().split())

if h == 1:
    print("1 " * c + "9 " * d)
    exit()


if w == 1:
    if h > 2:
        print(-1)
        exit()
    elif h == 2:
        if c == 1 and d == 1:
            print("1\n9")
            exit()
        else:
            print(-1)
            exit()
    if h == 1:
        print(1 if c != 0 else 9)
        exit()


if h * (h - 1) // 2 > min(c, d):
    print(-1)
    exit()


ans = [[1 for _ in range(w)] for __ in range(h)]
n = 0
y = h-1
x = 0

f = True
while f:
    sx = x
    sy = y
    while min(sy, sx) >= 0:
        ans[sy][sx] = 9

        n += 1
        if n == d:
            f = False
            break

        sx -= 1
        sy -= 1
    x += 1


for i in ans:
    print(*i)
