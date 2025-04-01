k = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

ans = 0
for i in a:
    for j in b:
        if i + k == j:
            ans += 1

print(ans)
