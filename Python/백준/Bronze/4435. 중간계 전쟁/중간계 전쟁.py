import sys

input = sys.stdin.readline

for t in range(int(input())):
    g = list(map(int, input().split()))
    s = list(map(int, input().split()))

    gs = 0
    ss = 0
    gw = [1, 2, 3, 3, 4, 10]
    sw = [1, 2, 2, 2, 3, 5, 10]
    for i in range(6):
        gs += g[i] * gw[i]

    for i in range(7):
        ss += s[i] * sw[i]

    print(f"Battle {t+1}: ", end="")
    if gs > ss:
        print("Good triumphs over Evil")
    elif gs < ss:
        print("Evil eradicates all trace of Good")
    else:
        print("No victor on this battle field")
