n = int(input())
x, y = 0, 0

f = True
for i in range(n):
    a, b = map(int, input().split())

    if x <= a and y <= b:
        x = a
        y = b
    else:
        f = False
        break

if f:
    print("yes")
else:
    print("no")
