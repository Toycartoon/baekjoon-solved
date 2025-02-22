import sys

input = sys.stdin.readline

for t in range(int(input())):
    s1, s2 = 0, 0
    for n in range(int(input())):
        p1, p2 = input().strip().split()

        if p1 == "R":
            if p2 == "P":
                s2 += 1
            elif p2 == "S":
                s1 += 1
        elif p1 == "P":
            if p2 == "S":
                s2 += 1
            elif p2 == "R":
                s1 += 1
        elif p1 == "S":
            if p2 == "R":
                s2 += 1
            elif p2 == "P":
                s1 += 1


    if s1 > s2:
        print("Player 1")
    elif s1 < s2:
        print("Player 2")
    else:
        print("TIE")