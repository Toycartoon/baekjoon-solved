while True:
    a, b = input().split()

    if a == b == "0":
        break

    ans = 0
    carry = 0
    a = a.zfill(max(len(a), len(b)))
    b = b.zfill(max(len(b), len(a)))
    for i in range(min(len(a), len(b))-1, -1, -1):
        if int(a[i]) + int(b[i]) + carry >= 10:
            ans += 1
            carry = 1
        else:
            carry = 0

    print(ans)
