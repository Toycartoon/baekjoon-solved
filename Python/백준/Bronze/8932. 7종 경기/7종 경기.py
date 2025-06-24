from math import trunc

def track(a, b, c, p):
    return trunc(a * pow(b - p, c))

def field(a, b, c, p):
    return trunc(a * pow(p - b, c))

for t in range(int(input())):
    p = list(map(int, input().split()))

    ans = 0
    w = [(True, 9.23076, 26.7, 1.835), (False, 1.84523, 75, 1.348), (False, 56.0211, 1.5, 1.05),
         (True, 4.99087, 42.5, 1.81), (False, 0.188807, 210, 1.41), (False, 15.9803, 3.8, 1.04),
         (True, 0.11193, 254, 1.88)]

    for i in range(7):
        if w[i][0]:
            ans += track(*w[i][1:], p[i])
        else:
            ans += field(*w[i][1:], p[i])

    print(ans)
