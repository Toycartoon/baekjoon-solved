import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    a = list(input().split())
    ans = a[0]
    
    for i in range(1, n):
        if ans[0] >= a[i]:
            ans = a[i] + ans
        else:
            ans += a[i]
    
    print(ans)
