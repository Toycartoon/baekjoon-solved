n = int(input())
strl = {}
for _ in range(n):
    p, P = input().split()
    strl[P] = p

ds = input()
s, e = map(int, input().split())
ans = ""
for i in ds:
    ans += strl[i]

print(ans[s-1:e])