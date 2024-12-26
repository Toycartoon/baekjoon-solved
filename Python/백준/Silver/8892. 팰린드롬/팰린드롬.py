from itertools import permutations as p
import sys

input = sys.stdin.readline

for t in range(int(input())):
    l = []
    for k in range(int(input())):
        l.append(input().strip())

    f = "0"
    for i in p(l, 2):
        s = "".join(i)
        
        if s == s[::-1]:
            f = s
            break

    print(f)
