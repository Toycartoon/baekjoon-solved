n = int(input())
a = list(map(int, input().split()))

jh, sm = n, n
jh_stock, sm_stock = 0, 0
for i in a:
    if jh // i >= 1:
        jh_stock += jh // i
        jh %= i


for i in range(len(a)):
    if i >= 3 and a[i-3] < a[i-2] < a[i-1] < a[i]:
        sm += a[i] * sm_stock
        sm_stock = 0
    elif i >= 3 and a[i-3] > a[i-2] > a[i-1] > a[i]:
        sm_stock += sm // a[i]
        sm %= a[i]


jh = jh + a[-1] * jh_stock
sm = sm + a[-1] * sm_stock

if jh > sm:
    print("BNP")
elif sm > jh:
    print("TIMING")
else:
    print("SAMESAME")
