n, m = map(int, input().split())

p = {}
nl = []
for _ in range(n):
    s = input()
    p[s] = _ + 1
    nl.append(s)

for _ in range(m):
    a = input()
    if a.isalpha():
        print(p[a])
    else:
        print(nl[int(a) - 1])