n, m, k = map(int, input().split())
s = []
for i in range(n):
    s.append(sorted([*input()]))

s.sort()
ans = []
for i in s[:k]:
    ans.extend([*i])

print("".join(sorted(ans)))
