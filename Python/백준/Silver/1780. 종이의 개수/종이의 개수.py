n = int(input())
arr = [0, 0, 0]

g = [list(map(int, input().split())) for _ in range(n)]

def f(n, x, y):
    s = g[y][x]
    fl = True
    
    for dy in range(n):
        for dx in range(n):
            if g[y+dy][x+dx] != s:
                fl = False

    if fl:
        if s == -1:
            arr[0] += 1
        elif s == 0:
            arr[1] += 1
        elif s == 1:
            arr[2] += 1
    else:
        a = n // 3
        f(a, x, y)
        f(a, x, y + a)
        f(a, x, y + 2 * a)
        f(a, x + a, y)
        f(a, x + a, y + a)
        f(a, x + a, y + 2 * a)
        f(a, x + 2 * a, y)
        f(a, x + 2 * a, y + a)
        f(a, x + 2 * a, y + 2 * a)


f(n, 0, 0)
for i in arr:
    print(i)
