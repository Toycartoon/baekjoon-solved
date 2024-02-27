import decimal

decimal.getcontext().prec = 35

n = int(input())
a = 0
ans = "0"
while a < n:
    s = input()
    if s == "0":
        a += 1
        x = len(str(ans))
        for i in range(len(str(ans))-1, -1, -1):
            if str(ans)[i] == "0":
                x -= 1
            else:
                if str(ans)[i] == ".":
                    x -= 1
                break
        print(str(ans)[:x])
        ans = "0"
        continue
    ans = decimal.Decimal(str(ans)) + decimal.Decimal(s)
