from math import sqrt

while True:
    try:
        r, s = map(float, input().split())
        v = sqrt((r * (s + 0.16)) / 0.067)

        print(round(v))
    except EOFError:
        break
