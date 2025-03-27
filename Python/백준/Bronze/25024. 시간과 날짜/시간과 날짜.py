import sys

input = sys.stdin.readline

for t in range(int(input())):
    x, y = map(int, input().split())
    
    if 0 <= x <= 23 and 0 <= y <= 59:
        print("Yes", end=" ")
    else:
        print("No", end=" ")
    
    w = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if 1 <= x <= 12 and 1 <= y <= w[x-1]:
        print("Yes")
    else:
        print("No")
