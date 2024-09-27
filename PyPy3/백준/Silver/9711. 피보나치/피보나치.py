import sys

input = sys.stdin.readline

for t in range(1, int(input())+1):
    p, q = map(int, input().split())

    i, j = 1, 1
    for x in range(1, p):
        if x % 2 == 1:
            i = (i + j) % q
        else:
            j = (i + j) % q


    print(f"Case #{t}:", end=" ")
    if q == 1:
        print(0)
        continue

    if p % 2 == 0:
        print(j)
    else:
        print(i)
