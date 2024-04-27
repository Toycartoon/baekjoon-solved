import sys

for _ in range(int(input())):
    a, b, c = map(int, sys.stdin.readline().split())

    sys.stdout.write(f"{min(((a + b) ** 2) + (c ** 2), ((b + c) ** 2) + (a ** 2), ((a + c) ** 2) + (b ** 2))}\n")