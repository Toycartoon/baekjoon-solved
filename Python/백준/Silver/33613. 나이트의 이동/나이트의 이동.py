from math import trunc

n = int(input())
r, c = map(int, input().split())

if n > 3:
    if n % 2 == 0:
        print((n // 2) * n)
    else:
        if (r+c) % 2 == 0:
            print(trunc((n ** 2) / 2) + 1)
        else:
            print(trunc((n ** 2) / 2))
elif n == 3 and not (r == 2 and c == 2):
    print(4)
else:
    print(1)
