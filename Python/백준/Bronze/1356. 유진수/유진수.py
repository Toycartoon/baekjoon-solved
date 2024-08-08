def mul(n):
    x = 1
    for i in n:
        x *= int(i)

    return x


n = input()
f = False
for i in range(1, len(n)):
    if mul(n[:i]) == mul(n[i:]):
        f = True
        break


if f:
    print("YES")
else:
    print("NO")
