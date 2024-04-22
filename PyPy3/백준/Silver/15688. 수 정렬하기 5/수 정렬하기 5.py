import sys

a = []
for _ in range(int(input())):
    a.append(int(sys.stdin.readline()))

a.sort()
for i in a:
    sys.stdout.write(f"{i}\n")