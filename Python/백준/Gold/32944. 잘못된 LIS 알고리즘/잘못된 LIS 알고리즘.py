n, m, k = map(int, input().split())

if m == n:
    print(-1)
    exit()

for i in range(1, k):
    print(i, end=" ")

print(n, end=" ")
for i in range(k, m):
    print(i, end=" ")

for i in range(n-1, m-1, -1):
    print(i, end=" ")
