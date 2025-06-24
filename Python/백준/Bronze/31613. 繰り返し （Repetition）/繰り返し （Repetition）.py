x = int(input())
n = int(input())

ans = 0
while x < n:
    r = x % 3

    if r == 0:
        x += 1
    elif r == 1:
        x *= 2
    elif r == 2:
        x *= 3

    ans += 1

print(ans)