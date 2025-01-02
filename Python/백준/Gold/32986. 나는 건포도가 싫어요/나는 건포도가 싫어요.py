x, y, z = map(int, input().split())

if x == y == z == 3:
    print(0)
else:
    print(min((x-1)//2, (y-1)//2, (z-1)//2))