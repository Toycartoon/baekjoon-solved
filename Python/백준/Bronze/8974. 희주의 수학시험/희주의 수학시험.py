a, b = map(int, input().split())

i = 1
n = []
while len(n) <= b:
    if n.count(i) == i:
        i += 1
    n.append(i)

print(sum(n[a-1:b]))