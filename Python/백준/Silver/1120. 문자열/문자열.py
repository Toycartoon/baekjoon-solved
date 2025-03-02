from math import inf

a, b = input().split()

ans = inf
for i in range(len(b)-len(a)+1):
    x = 0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            x += 1

    ans = min(ans, x)

print(ans)