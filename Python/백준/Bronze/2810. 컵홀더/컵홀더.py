n = int(input())
s = input()

ans = 1
i = 0
while i < n:
    if s[i] == "S":
        ans += 1
    elif s[i] == "L":
        ans += 1
        i += 1
    i += 1


print(min(ans, n))
