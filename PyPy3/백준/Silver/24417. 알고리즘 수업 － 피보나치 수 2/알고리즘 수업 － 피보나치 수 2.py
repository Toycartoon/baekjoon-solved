code2 = 0
n = int(input())
f, g = 1, 1

for i in range(2, n):
    if i % 2 == 0:
        f += g
        f %= 1000000007
    else:
        g += f
        g %= 1000000007
    code2 += 1

print(g % 1000000007 if n % 2 == 0 else f % 1000000007, code2 % 1000000007)
