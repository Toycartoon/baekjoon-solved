import sys

input = sys.stdin.readline

ans = []
for n in range(int(input())):
    r1, r2, *t = map(int, input().split())
    
    ans.append(max(r1, r2) + sum(sorted(t, reverse=True)[:2]))

print(max(ans))