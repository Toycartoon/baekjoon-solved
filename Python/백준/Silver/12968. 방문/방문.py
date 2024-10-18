r, c, k = map(int, input().split())

if r * c % 2 == 0:
    print(1)
else:
    if k != 1:
        print(0)
    else:
        print(1)