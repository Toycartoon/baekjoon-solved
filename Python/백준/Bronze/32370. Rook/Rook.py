a, b = map(int, input().split())
x, y = map(int, input().split())

if a == 0:
    if x == 0 and 0 < y < b:
        print(3)
    else:
        print(1)
elif b == 0:
    if y == 0 and 0 < x < a:
        print(3)
    else:
        print(1)
else:
    print(2)
