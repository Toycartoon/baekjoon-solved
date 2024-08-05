n = int(input())
h = list(map(int, input().split()))
ans = 1

b = 0
for i in h:
    if i >= b and b != 0:
        ans += 1

    b = i

print(ans)
