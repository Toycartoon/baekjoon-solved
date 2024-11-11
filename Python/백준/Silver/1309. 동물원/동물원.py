n = int(input())

f, g = 3, 7
for i in range(1, n):
    if i % 2 == 0:
        g = (2 * f + g) % 9901
    else:
        f = (2 * g + f) % 9901
        
if n % 2 == 0:
    print(g)
else:
    print(f)