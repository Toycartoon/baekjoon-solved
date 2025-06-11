import sys

input = sys.stdin.readline

while True:
    s = input().strip()

    if s == "#":
        break

    if s[-1] == "o" and s.count("1") % 2 == 0 or s[-1] == "e" and s.count("1") % 2 == 1:
        print(s[:-1] + "1")
    else:
        print(s[:-1] + '0')
