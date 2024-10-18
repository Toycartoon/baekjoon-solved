from math import trunc, ceil


n = int(input())

if n == 3:
    print(-1)
    exit()


if n % 2 == 0:
    for i in range(n-1, n*2-1):
        print(i % n if i % n != 0 else n)
else:
    for i in range(n):
        if i == n-1:
            print(ceil(n / 2) + 1)
        elif i == trunc(n / 2):
            print(1)
        else:
            print(i+2)
