n, m = map(int, input().split())
a, b = list(map(int, input().split()))

c = a
for i in range(m):
    k = int(input())
    if c <= k:
        if c == a:
            c = b
        else:
            c = a

print(c)
