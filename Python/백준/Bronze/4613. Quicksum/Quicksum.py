import sys

input = sys.stdin.readline

while True:
    s = input().strip()

    if s == "#":
        break

    ans = 0
    for i in range(len(s)):
        ans += (i + 1) * (ord(s[i]) - 64 if s[i].isalpha() else 0)

    print(ans)
