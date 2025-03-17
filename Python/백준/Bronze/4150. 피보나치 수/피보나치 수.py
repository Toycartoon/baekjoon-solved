f = 1
g = 1

n = int(input())
for i in range(1, n):
    if i % 2 == 1:
        f += g
    else:
        g += f

if n % 2 == 1:
    print(f)
else:
    print(g)
