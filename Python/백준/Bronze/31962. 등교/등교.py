n, x = map(int, input().split())
ans = []

for i in range(n):
    s, t = map(int, input().split())
    if s + t <= x:
        ans.append(s)
    
if len(ans) == 0:
    print(-1)
else:
    print(max(ans))
