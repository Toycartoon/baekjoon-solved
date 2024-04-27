n, p = map(int, input().split())

a = 1
for i in range(2, n + 1):
    a *= i
    a %= p

print(a)