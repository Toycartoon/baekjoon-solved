f, g = 1, 1
n = int(input())

if n == 1:
    print(4)
    exit()

for i in range(1, n-1):
    if i % 2 == 1:
        f += g
    else:
        g += f


if n % 2 == 0:
    print(g * 2 + (f + g) * 2)
else:
    print(f * 2 + (f + g) * 2)