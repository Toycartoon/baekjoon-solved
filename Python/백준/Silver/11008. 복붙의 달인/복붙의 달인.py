import sys

input = sys.stdin.readline

for t in range(int(input())):
    s, p = input().strip().split()

    ans = s.count(p)
    s = s.replace(p, "")
    ans += len(s)
    
    print(ans)
