t = int(input())

ans = ""
while t >= 9:
    m = t % 9
    t //= 9

    ans += str(m)

m = t % 9
ans += str(m)

print(ans[::-1])
