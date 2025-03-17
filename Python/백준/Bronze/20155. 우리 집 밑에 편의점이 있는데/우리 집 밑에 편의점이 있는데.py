n, m = map(int, input().split())
x = list(map(int, input().split()))

ans = [0 for _ in range(m+1)]
for i in x:
    ans[i] += 1

print(max(ans))
