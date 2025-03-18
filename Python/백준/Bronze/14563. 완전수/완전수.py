t = int(input())
n = list(map(int, input().split()))

for i in n:
    a = 0
    for x in range(i // 2, 0, -1):
        if i % x == 0:
            a += x

    if a == i:
        print("Perfect")
    elif a < i:
        print("Deficient")
    else:
        print("Abundant")
