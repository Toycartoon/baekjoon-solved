n = int(input())
x = 0
f = True
for i in range(n):
    a = int(input())

    if a - x != 1:
        [print(t) for t in range(x+1, a)]
        f = False

    x = a

if f:
    print("good job")
