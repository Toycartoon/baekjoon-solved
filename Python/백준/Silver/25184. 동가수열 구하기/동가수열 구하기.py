from math import trunc

n = int(input())
x = trunc(n / 2)

for i in range(n-x, 0, -1):
    if i == 1 and n % 2 == 1:
        print(i)
        break
    print(i, i+x, end=' ')
