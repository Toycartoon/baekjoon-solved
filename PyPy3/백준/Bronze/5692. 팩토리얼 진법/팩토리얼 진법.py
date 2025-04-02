from math import factorial as f
import sys

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    a = 0
    for i in range(len(str(n)) - 1, -1, -1):
        a += int(str(n)[len(str(n)) - (i + 1)]) * f(i + 1)

    sys.stdout.write(f"{a}\n")