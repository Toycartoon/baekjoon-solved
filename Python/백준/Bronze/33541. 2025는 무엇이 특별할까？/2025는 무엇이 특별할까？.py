x = int(input())

f = True
for y in range(x+1, 10000):
    if y == ((y // 100) + (y % 100)) ** 2:
        print(y)
        f = False
        break

if f:
    print(-1)
