a, b, c = map(int, input().split())

ans = 0
coin = 0
while coin < c:
    coin += a
    ans += 1
    if ans % 7 == 0:
        coin += b

print(ans)
