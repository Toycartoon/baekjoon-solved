n = int(input())
ans = [True for _ in range(n-1)]

for i in range(int(input())):
    x, y = map(int, input().split())

    for j in range(x-1, y-1):
        ans[j] = False

print(ans.count(True) + 1)

