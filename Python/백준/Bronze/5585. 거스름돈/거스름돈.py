c = [500, 100, 50, 10, 5, 1]

m = 1000 - int(input())

n = 0
for i in c:
    n += int(m // i)
    m = m % i

print(n)