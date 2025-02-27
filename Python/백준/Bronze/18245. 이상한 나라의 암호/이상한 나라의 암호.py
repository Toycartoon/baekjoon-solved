import sys

input = sys.stdin.readline

i = 2
while True:
    s = input().strip()

    if s == "Was it a cat I saw?":
        break

    for t in range(0, len(s), i):
        print(s[t], end="")

    print()
    i += 1
