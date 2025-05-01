import sys

input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())

    if n % 2 != 0:
        print("NIE")
        continue

    e = 0
    while n > 1:
        if n % 2 == 0:
            e += 1
            n //= 2
        else:
            break

    if e % 2 == 0:
        print("NIE")
    else:
        print("TAK")
