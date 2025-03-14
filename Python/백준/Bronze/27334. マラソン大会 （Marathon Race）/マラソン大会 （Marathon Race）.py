n = int(input())
a = list(map(int, input().split()))

ans = [1 for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            continue

        if a[i] > a[j]:
            ans[i] += 1


for i in ans:
    print(i)
