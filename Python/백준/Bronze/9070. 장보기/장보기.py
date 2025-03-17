import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    ans = []

    for i in range(n):
        w, c = map(int, input().split())
        ans.append((w / c, c))

    ans.sort(key=lambda x: (-x[0], x[1]))
    print(ans[0][1])
