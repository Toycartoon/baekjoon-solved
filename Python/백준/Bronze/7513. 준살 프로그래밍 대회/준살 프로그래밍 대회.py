import sys

input = sys.stdin.readline

for t in range(int(input())):
    m = int(input())
    w = []
    for i in range(m):
        w.append(input().strip())

    print(f"Scenario #{t+1}:")
    for n in range(int(input())):
        k, *x = map(int, input().split())

        for i in x:
            print(w[i], end="")
        print()

    print()