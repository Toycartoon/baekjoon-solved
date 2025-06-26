from decimal import Decimal as d

t = 0
for i in range(int(input())):
    a, b, c, w = map(d, input().split())

    if ((a <= d("56") and b <= d("45") and c <= d("25")) or (a + b + c <= d("125"))) and w <= d("7"):
        print(1)
        t += 1
    else:
        print(0)

print(t)
