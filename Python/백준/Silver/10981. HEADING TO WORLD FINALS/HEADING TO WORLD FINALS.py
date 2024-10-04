n, k = map(int, input().split())
l = []
for i in range(n):
    univ, name, s, p = input().split()
    l.append((int(s), int(p), name, univ))

l = sorted(sorted(l, key=lambda x: x[1]), key=lambda x: x[0], reverse=True)
a = set()
for i in range(n):
    if l[i][3] not in a:
        a.add(l[i][3])
        print(l[i][2])
        
        if len(a) == k:
            break