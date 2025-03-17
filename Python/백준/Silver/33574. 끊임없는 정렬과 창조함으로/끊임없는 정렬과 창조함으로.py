import sys

input = sys.stdin.readline

s = []
q = []
ls = -1

for i in range(int(input())):
    c, x, *t = map(int, input().split())

    if c == 1:
        ls = i

    q.append((c, x, t))

for x in range(len(q)):
    i = q[x]
    if x == ls:
        if i[1] == 1:
            s.sort()
        elif i[1] == 2:
            s.sort(reverse=True)
    if i[0] == 2:
        s.insert(i[1], i[2][0])

print(len(s))
print(*s)
