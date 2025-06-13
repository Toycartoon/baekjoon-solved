import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    p.sort(reverse=True)

    ans = []
    x = set()
    for i in range(n * 2):
        if p[i]:
            ans.append(p[i] - (p[i] // 4))
            p[p.index(p[i] - (p[i] // 4))] = 0

    print(f"Case #{t+1}:", *sorted(ans))
