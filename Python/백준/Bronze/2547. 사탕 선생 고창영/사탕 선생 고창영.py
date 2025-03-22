import sys

input = sys.stdin.readline

for t in range(int(input())):
    _ = input()
    n = int(input())

    a = []
    for i in range(n):
        a.append(int(input()))

    if sum(a) % n == 0:
        print("YES")
    else:
        print('NO')
