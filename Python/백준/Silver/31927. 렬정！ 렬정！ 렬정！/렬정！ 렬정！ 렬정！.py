n = int(input())
a = list(map(int, input().split()))

if sorted(a, reverse=True) == a:
    print(0)
    exit()


print(n // 2)
w = 10 ** 6 // (n // 2)
x = w
for i in range(n // 2 - 1, -1, -1):
    a[i] += x
    a[n-i-1] -= x

    x += w
    print(*a)
