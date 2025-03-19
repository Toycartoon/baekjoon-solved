cu, du = map(int, input().split())
cd, dd = map(int, input().split())
cp, dp = map(int, input().split())
h = int(input())

ans = 0
while True:
    if ans % cu == 0:
        h -= du
    if ans % cd == 0:
        h -= dd
    if ans % cp == 0:
        h -= dp

    if h <= 0:
        print(ans)
        break
    ans += 1
