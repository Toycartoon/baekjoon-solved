import sys

input = sys.stdin.readline

while True:
    s = input().strip()

    if s == "#":
        break

    w = [False for _ in range(26)]
    for i in s.lower():
        if i.isalpha():
            w[ord(i)-97] = True

    print(w.count(True))