import sys

input = sys.stdin.readline

w = {}
for n in range(int(input())):
    a, b = input().strip().split()
    w[a] = b

ans = ""
for i in range(int(input())):
    x = input().strip()

    if x in w:
        ans += w[x]
    else:
        ans += x

print(ans)
