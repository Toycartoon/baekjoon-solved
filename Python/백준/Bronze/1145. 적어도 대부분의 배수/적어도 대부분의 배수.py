n = list(map(int, input().split()))
a = sorted(n)[2]

while True:
    i = 0
    for j in n:
        if a % j == 0:
            i += 1
    if i >= 3:
        break
    a += 1

print(a)