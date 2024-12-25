import sys

input = sys.stdin.readline

v = {}
while True:
    s = input().strip()
    
    if s == "***":
        break
    
    if s in v:
        v[s] += 1
    else:
        v[s] = 1

f = True
m = max(v.values())
ans = ""
for i in v.keys():
    if v[i] == m:
        if ans == "":
            ans = i
        else:
            f = False
            break
            
            
print(ans if f else "Runoff!")