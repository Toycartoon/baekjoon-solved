import sys

input = sys.stdin.readline

while True:
    n = int(input())

    if n == 0:
        break

    if n <= 1000000:
        print(n)
    elif 1000000 < n <= 5000000:
        print(n - (n // 10))
    else:
        print(n - (n // 100 * 20))
