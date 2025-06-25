p, q = map(int, input().split())

a = []
b = []
for i in range(1, p+1):
    if p % i == 0:
        a.append(i)

for i in range(1, q+1):
    if q % i == 0:
        b.append(i)

for i in a:
    for j in b:
        print(i, j)
