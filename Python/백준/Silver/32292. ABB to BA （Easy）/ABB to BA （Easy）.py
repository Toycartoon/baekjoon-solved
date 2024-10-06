import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    s = input().strip()

    while True:
        if "ABB" not in s:
            break
        s = s.replace("ABB", "BA")

    print(s)
