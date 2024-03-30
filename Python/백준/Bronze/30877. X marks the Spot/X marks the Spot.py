import sys

input = sys.stdin.readline

for _ in range(int(input())):
    s, t = input().split()
    for i in range(len(s)):
        if s[i].upper() == "X":
            sys.stdout.write(t[i].upper())
            break