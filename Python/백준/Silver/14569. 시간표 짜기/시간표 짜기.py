import sys

input = sys.stdin.readline

sub = []
n = int(input())
for i in range(n):
    k, *t = map(int, input().split())
    sub.append(set(t))

for i in range(int(input())):
    p, *q = map(int, input().split())
    ans = 0
    for x in sub:
        if len(set(q) - x) == p - len(x):
            ans += 1

    print(ans)
