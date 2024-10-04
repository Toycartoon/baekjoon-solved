f, g = 0, 1
n = int(input())

for i in range(1, n):
    if i % 2 == 0:
        g += f
        g %= 1000000007
    else:
        f += g
        f %= 1000000007

if n % 2 == 0:
    print(f)
else:
    print(g)