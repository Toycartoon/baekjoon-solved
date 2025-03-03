import sys

input = sys.stdin.readline

for k in range(int(input())):
    p, m = map(int, input().split())
    w = [False for _ in range(m+1)]

    ans = 0
    for i in range(p):
        n = int(input())

        if w[n]:
            ans += 1
        else:
            w[n] = True
        
    print(ans)
