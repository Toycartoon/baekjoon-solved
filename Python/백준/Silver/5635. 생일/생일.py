n = int(input())
l = []
for _ in range(n):
    a, d, m, y = input().split()
    l.append((a, int(y), int(m), int(d)))

l.sort(key=lambda x: (x[1], x[2], x[3]))
print(l[-1][0])
print(l[0][0])
