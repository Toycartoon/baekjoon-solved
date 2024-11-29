n = int(input())

if n <= 10:
    print(1)
    exit()

for i in range(9, 1, -1):
    for j in range(9, 0, -1):
        if i * j == n:
            print(1)
            exit()

print(0)