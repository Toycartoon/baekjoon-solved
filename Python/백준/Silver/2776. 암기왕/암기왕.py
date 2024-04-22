import sys

for _ in range(int(input())):
    n = int(input())
    o = set(map(int, sys.stdin.readline().split()))
    m = int(input())
    t = list(map(int, sys.stdin.readline().split()))

    for i in t:
        if i in o:
            sys.stdout.write("1\n")
        else:
            sys.stdout.write("0\n")