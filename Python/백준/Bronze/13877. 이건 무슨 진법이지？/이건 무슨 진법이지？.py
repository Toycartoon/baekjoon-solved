import sys

input = sys.stdin.readline

for t in range(int(input())):
    i, k = input().strip().split()

    try:
        print(i, int(k, 8), int(k), int(k, 16))
    except ValueError:
        print(i, 0, int(k), int(k, 16))
