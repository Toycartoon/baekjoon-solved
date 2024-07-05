n = int(input())
a = 0
for i in range(1, n+1):
    a += i * (i + 1) // 2 + i * (i + 1)

print(a)