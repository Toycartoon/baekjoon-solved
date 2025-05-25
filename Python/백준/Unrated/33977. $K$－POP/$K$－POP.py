from math import inf

n = int(input())

a = 1
b = n
mn = inf
for i in range(n // 2, 0, -1):
    if n % i == 0:
        j = n // i
        if min(abs(i - j), mn) == abs(i - j):
            mn = abs(i - j)
            a = i
            b = j

if mn == n-1 and n != 2:
    print(n+1)
    for i in range(1, n+1):
        print(i, i+1)
    exit()

if a < b:
    a, b = b, a

print(a + b)
for i in range(1, a+1):
    print(i, i+1)

for i in range(b-1):
    print(i+1, i+a+2)
