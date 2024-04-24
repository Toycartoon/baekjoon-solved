n, m = map(int, input().split())
r = []
c = []
for _ in range(n):
    s = input()
    t = ""
    for i in range(m):
        t += s[i] * 2
    r.append(t)
for _ in range(n):
    c.append(input())

f = False
for i in range(n):
    if r[i] != c[i]:
        f = True

if f:
    print("Not Eyfa")
else:
    print("Eyfa")