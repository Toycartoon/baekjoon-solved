f, g = 1, 1
n = int(input())

if n < 2:
    print(1)
    exit()

for i in range(1, n):
    if i % 2 == 0:
        g += f + 1
        g %= 1000000007
    else:
        f += g + 1
        f %= 1000000007

if n % 2 == 0:
    print(f)
else:
    print(g)