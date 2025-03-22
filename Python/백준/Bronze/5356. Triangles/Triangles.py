import sys

input = sys.stdin.readline

for t in range(int(input())):
    n, s = input().strip().split()

    s = ord(s)
    for i in range(int(n)):
        print(chr(s) * (i+1))
        s += 1

        if s > 90:
            s = 65
    print()
