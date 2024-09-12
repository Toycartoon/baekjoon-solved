import sys


input = sys.stdin.readline

for t in range(int(input())):
    n = input().strip()

    x = 0
    for i in n:
        x += int(i)

    if x % 9 == 0:
        print("YES")
    else:
        print("NO")

