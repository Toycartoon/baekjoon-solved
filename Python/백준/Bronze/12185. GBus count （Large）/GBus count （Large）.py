import sys

input = sys.stdin.readline

mt = int(input())
for t in range(mt):
    n = int(input())
    a = list(map(int, input().split()))
    c = []
    for i in range(int(input())):
        c.append(int(input()))

    print(f"Case #{t+1}: ", end='')
    for i in c:
        ans = 0
        for x in range(0, n*2, 2):
            if a[x] <= i <= a[x+1]:
                ans += 1
        print(ans, end=" ")
    print()
    input()
