n = int(input())
a = list(map(int, input().split()))
x, y = map(int, input().split())

a.sort()
z = 0
for i in range(n):
    if a[i] >= y:
        z += 1

print(n * x // 100, z)