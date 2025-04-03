import sys

input = sys.stdin.readline

t = 1
while True:
    n = int(input())

    if n == 0:
        break

    print(f"User {t}")
    for i in range(int(input())):
        x = int(input())
        print("{:.05f}".format(x * n / 100000))

    t += 1
