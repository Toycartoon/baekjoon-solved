import sys

input = sys.stdin.readline

t = []
for n in range(int(input()) + 1):
    a, k = input().split()

    h, m = a.split(":")
    t.append((int(h), int(m), "a" if k == "teacher" else "b"))

tm = input().split(":")
t.append((int(tm[0]), int(tm[1]), "-"))

t.sort()
ans = 0
late = False
teacher = False
for i in t:
    if i[2] == "-":
        late = True
    if i[2] == "a":
        teacher = True
    if i[2] == "b":
        if late and teacher:
            ans += 1


print(ans)