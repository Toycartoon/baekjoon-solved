n, k = map(int, input().split())

m = []
for _ in range(n):
    m.append(int(input()))

m.reverse()
a = 0
for _ in range(n):
    a += int(k // m[_])
    k = k % m[_]

print(a)