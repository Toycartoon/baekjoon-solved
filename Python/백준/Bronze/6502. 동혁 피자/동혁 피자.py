import sys

input = sys.stdin.readline

t = 1
while True:
    r, *x = map(int, input().split())

    if r == 0:
        break

    w, l = x
    if r * 2 >= (w ** 2 + l ** 2) ** 0.5:
        print(f"Pizza {t} fits on the table.")
    else:
        print(f"Pizza {t} does not fit on the table.")

    t += 1
