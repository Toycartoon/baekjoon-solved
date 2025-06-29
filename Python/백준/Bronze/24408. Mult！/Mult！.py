n = int(input())
b = 0

for i in range(n):
    v = int(input())

    if b == 0:
        b = v
    elif v % b == 0:
        print(v)
        b = 0
