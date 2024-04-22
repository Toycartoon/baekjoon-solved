x1, x2 = map(int, input().split())
a, b, c, d, e = map(int, input().split())

f = [a // 3, (b - d) // 2, c - e]

fx1, fx2 = 0, 0
for i in range(len(f)):
    fx1 += f[i] * (x1 ** (3 - i))
    fx2 += f[i] * (x2 ** (3 - i))

print(fx2 - fx1)