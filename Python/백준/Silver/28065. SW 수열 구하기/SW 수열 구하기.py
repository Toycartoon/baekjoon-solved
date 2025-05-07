n = int(input())
v = n-1

print(1, end=" ")
x = 1
for i in range(n-1):
    if i % 2 == 0:
        x += v
        v -= 1
    else:
        x -= v
        v -= 1

    print(x, end=" ")
