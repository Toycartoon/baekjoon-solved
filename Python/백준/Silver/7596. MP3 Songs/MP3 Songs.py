import sys

input = sys.stdin.readline

t = 1
while True:
    n = int(input())

    if n == 0:
        break
    
    l = []
    for i in range(n):
        l.append(input().strip())

    l.sort()
    print(t)
    for i in l:
        print(i)

    t += 1
