n = int(input())

f, g = 1, 3
if n % 2 == 1:
    print(0)
    exit()

for i in range(1, n // 2 + 1):
    if i % 2 == 1:
        f = 4 * g - f
    else:
        g = 4 * f - g


if n % 4 == 0:
    print(f)
else:
    print(g)
