n = int(input())
y, m = 2024, 8

for i in range(n-1):
    m += 7
    if m > 12:
        m -= 12
        y += 1

print(y, m)
