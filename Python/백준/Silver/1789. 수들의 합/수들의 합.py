s = int(input())

n = 0
a = 0
while True:
    n += 1
    a += n
    if a > s:
        break

print(n-1)