from sys import stdin

k = int(stdin.readline())
c = int(stdin.readline())

for i in range(c):
    m, n = map(int, stdin.readline().split())
    gap = abs(m - n)    # 절댓값
    remainRound = k - max(m, n)
    if m == n:
        print(1)
    elif m < n:
        if gap - remainRound <= 1:
            print(1)
        else:
            print(0)
    else:
        if gap - remainRound <= 2:
            print(1)
        else:
            print(0)