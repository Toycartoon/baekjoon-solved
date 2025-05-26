n = int(input())
b = len(str(n))

n *= 2
ans = 0

while b == len(str(n)):
    b = len(str(n))
    n *= 2
    ans += 1

print(ans)
