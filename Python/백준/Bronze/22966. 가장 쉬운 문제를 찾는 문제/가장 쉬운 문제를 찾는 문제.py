l = []
for i in range(int(input())):
    n, h = input().split()
    l.append((n, int(h)))

l.sort(key=lambda x: x[1])
print(l[0][0])
