n = int(input())
a = []

for i in range(n):
    a.append(tuple(map(int, input().split())))

a.sort()
for i in a:
    print(*i)
