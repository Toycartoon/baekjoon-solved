import sys

input = sys.stdin.readline

for i in range(int(input())):
    n, m = map(int, input().split())

    if n == 1 or m == 1:
        print("YES")
        continue
    else:
        if (n % 2 == 1 and m % 2 == 0) or (n % 2 == 0 and m % 2 == 1):
            print("YES")
        else:
            print("NO")
