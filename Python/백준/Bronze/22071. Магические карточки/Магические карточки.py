import sys

input = sys.stdin.readline

for t in range(int(input())):
    n, l = map(int, input().split())

    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())), reverse=True)

    if sum(a[:l]) > sum(b[:l]):
        print("YES")
    else:
        print("NO")
