import sys

input = sys.stdin.readline

ans = 0
for n in range(int(input())):
    a = int(input())
    
    if a != 1:
        ans += 1

print(ans)
