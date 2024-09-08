n = int(input())
a = list(map(int, input().split()))

ans = 1
b = [0] * n
while a != b:
    for i in range(1, n):
        for j in range(i):
            if a[j] < a[i]:
                b[j] += 1

    if a != b:
        a = b
        b = [0] * n
    ans += 1


print(ans)
