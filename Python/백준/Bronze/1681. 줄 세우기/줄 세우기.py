n, l = map(int, input().split())
i = 1
x = 1
while i <= n:
    if str(l) not in str(x):
        i += 1
    x += 1

print(x-1)
