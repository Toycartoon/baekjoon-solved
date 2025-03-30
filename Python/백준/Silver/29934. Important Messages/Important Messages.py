import sys

input = sys.stdin.readline

w = set()
for n in range(int(input())):
    w.add(input().strip())


ans = 0
for m in range(int(input())):
    s = input().strip()
    if s in w:
        ans += 1


print(ans)
