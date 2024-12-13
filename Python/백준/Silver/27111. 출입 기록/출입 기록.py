import sys

input = sys.stdin.readline

n = int(input())
r = set()

ans = 0
for i in range(n):
    a, b = map(int, input().split())

    if b == 1:
        if a in r:
            ans += 1
        else:
            r.add(a)
    elif b == 0:
        if a not in r:
            ans += 1
        else:
            r.remove(a)


ans += len(r)
print(ans)
