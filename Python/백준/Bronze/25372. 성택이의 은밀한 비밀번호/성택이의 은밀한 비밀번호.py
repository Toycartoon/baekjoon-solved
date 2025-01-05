n = int(input())

for _ in range(n):
    p = input()
    
    if 6 <= len(p) <= 9:
        print("yes")
    else:
        print("no")