import sys

input = sys.stdin.readline

for t in range(int(input())):
    s = input().strip()

    if s.startswith("Simon says"):
        print(s.split("Simon says")[1])
