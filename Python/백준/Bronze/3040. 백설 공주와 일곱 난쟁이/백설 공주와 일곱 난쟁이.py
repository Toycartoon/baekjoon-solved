from itertools import combinations as com

n = [int(input()) for _ in range(9)]
c = list(com(n, 7))

for i in c:
    if sum(i) == 100:
        for j in i:
            print(j)
        break