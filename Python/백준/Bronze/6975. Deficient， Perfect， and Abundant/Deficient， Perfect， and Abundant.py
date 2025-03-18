import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    a = 0
    for x in range(n // 2, 0, -1):
        if n % x == 0:
            a += x

    if a == n:
        print(n, "is a perfect number.")
    elif a < n:
        print(n, "is a deficient number.")
    else:
        print(n, "is an abundant number.")
    print()
