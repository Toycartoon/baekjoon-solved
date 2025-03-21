n = int(input())
f = [False, False, False]

for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a

    if a == 1 and b == 3:
        f[0] = True
    elif a == 1 and b == 4:
        f[1] = True
    elif a == 3 and b == 4:
        f[2] = True
    else:
        print("Woof-meow-tweet-squeek")
        exit()

if f.count(True) == 3:
    print("Wa-pa-pa-pa-pa-pa-pow!")
else:
    print("Woof-meow-tweet-squeek")
