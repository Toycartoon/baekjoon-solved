n = int(input())
print(n - 1 if (n // 2) % 2 == 1 else n)
for i in range(n-1, 1, -2):
    print(i, i-1)

for i in range(n // 4):
    print(1, 1)

for i in range(n // 4):
    print(0, n)

if (n // 2) % 2 == 1:
    print(1, n)
