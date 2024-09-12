import sys


input = sys.stdin.readline

g = [True] * 5000001
g[0] = False
g[1] = False
for i in range(2, int(5000001 ** 0.5)):
    if g[i]:
        for j in range(i * i, 5000001, i):
            g[j] = False


while True:
    n = int(input())
    a, b = -1, -1

    if n == 0:
        break

    for i in range(1, n // 2 + 1):
        if g[i] and g[n-i]:
            a, b = i, n-i
            break


    if a == b == -1:
        print("Goldbach's conjecture is wrong.")
        continue

    print(f"{n} = {a} + {b}")
