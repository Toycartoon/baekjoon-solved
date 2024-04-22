n = int(input())
l = list(map(int, input().split()))

sl = sorted(set(l))

d = {}
for i in range(len(sl)):
    d[sl[i]] = i

for i in l:
    print(d[i], end=" ")