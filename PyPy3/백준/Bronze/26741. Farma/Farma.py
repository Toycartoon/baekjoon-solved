x, y = map(int, input().split())

for i in range(x+1):
    if (2 * i) + (4 * (x - i)) == y:
        print(i, x - i)
        break
