n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

print(min(a.count(1), a.count(0)))
