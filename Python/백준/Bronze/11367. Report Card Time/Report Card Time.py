import sys

input = sys.stdin.readline

for n in range(int(input())):
    s, g = input().split()
    
    if int(g) >= 97:
        ans = "A+"
    elif int(g) >= 90:
        ans = "A"
    elif int(g) >= 87:
        ans = "B+"
    elif int(g) >= 80:
        ans = "B"
    elif int(g) >= 77:
        ans = "C+"
    elif int(g) >= 70:
        ans = "C"
    elif int(g) >= 67:
        ans = "D+"
    elif int(g) >= 60:
        ans = "D"
    else:
        ans = "F"
    
    print(s, ans)