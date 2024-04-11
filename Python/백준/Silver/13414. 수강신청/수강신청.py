import sys

input = sys.stdin.readline

k, l = map(int, input().split())
s = [input().strip() for _ in range(l)]

final_l = []
c = set()
for i in reversed(s):
    if i in c:
        continue

    c.add(i)
    final_l.append(i)

final_l.reverse()
for i in range(min(k, len(final_l))):
    print(final_l[i])
