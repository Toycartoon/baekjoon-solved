n = int(input())
m = int(input())

a = []
b = []
for i in range(n):
    a.append(input())

for i in range(m):
    b.append(input())

for x in a:
    for y in b:
        print(f"{x} as {y}")
