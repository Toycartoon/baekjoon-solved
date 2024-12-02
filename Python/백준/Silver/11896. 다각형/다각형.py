a, b = map(int, input().split())

a = ((a + 1) // 2) * 2
b = (b // 2) * 2

if a <= 2:
    a = 4

if b < a:
    print(0)
    exit()

c = ((b - a) // 2) + 1
print(c * (a + b) // 2)
