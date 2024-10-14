n = [i for i in range(100000)]

n[0] = -1
n[1] = -1

for i in range(2, int(len(n) ** 0.5)):
    if n[i] == -1:
        continue
    for j in range(i ** 2, len(n), i):
        n[j] = -1

for t in range(int(input())):
    k = int(input())

    a = k
    f = True
    while f:
        for x in range(2, a):
            if a % x == 0 and n[x] != -1 and n[a // x] != -1 and x != a // x:
                print(a)
                f = False
                break

        a += 1
