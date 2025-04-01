w = {}
n = int(input())
for i in range(n):
    s = input().strip()
    if s not in w:
        w[s] = 1
    else:
        w[s] += 1

mx = max(w.values())
ans = []
for i in w:
    if w[i] == mx:
        ans.append(i)

for i in sorted(ans):
    print(i)
