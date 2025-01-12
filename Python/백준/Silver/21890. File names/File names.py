import sys

input = sys.stdin.readline

ans = 0
for t in range(int(input())):
    s = input().strip()

    if len(s.split(".")) != 2:
        continue

    if 1 <= len(s.split(".")[0]) <= 8 and 1 <= len(s.split(".")[1]) <= 3:
        ans += 1

        
print(ans)
