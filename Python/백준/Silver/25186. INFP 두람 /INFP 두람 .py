from math import trunc

n = int(input())
l = list(map(int, input().split()))

if n == 1:
    if l[0] == 1:
        print("Happy")
        exit()
    else:
        print("Unhappy")
        exit()

if max(l) > trunc(sum(l) / 2):
    print("Unhappy")
else:
    print("Happy")