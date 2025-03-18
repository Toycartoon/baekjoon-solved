n = int(input())
a = list(map(int, input().split()))

x = 1
a.sort()
for i in a:
    if x == i:
        x += 1
    else:
        break

print(x)
