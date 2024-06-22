n, m = map(int, input().split())
s = []
a = []
for i in range(n):
    l = input().split()
    st = 0
    t = []
    for x in range(m):
        if  l[x] == ".":
            st += 1
        else:
            t.append(st)
            st = 0
    t.append(st)
    a.append(l[-1])
    s.append(max(t))

print(len(set(s)))
for i in range(n):
    print(s[i], a[i])
