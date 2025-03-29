import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())

    if n == 0:
        print(f"Case #{t+1}: INSOMNIA")
        continue

    x = [False for _ in range(10)]

    w = 1
    v = n
    for i in str(v):
        x[int(i)] = True

    while x.count(True) < 10:
        w += 1
        v = w * n

        for i in str(v):
            x[int(i)] = True

    print(f"Case #{t+1}: {v}")
