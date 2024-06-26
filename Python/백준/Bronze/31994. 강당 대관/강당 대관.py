l = []
for i in range(7):
    s, n = input().split()
    l.append((s, int(n)))

l.sort(key=lambda x: x[1], reverse=True)
print(l[0][0])
