n = int(input())
t = list(map(int, input().split()))

t.sort(reverse=True)
ans = []
for i in range(n):
    ans.append(t[i] + i + 1)


print(max(ans) + 1)
