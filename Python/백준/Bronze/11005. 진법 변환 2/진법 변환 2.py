n, b = map(int, input().split())
a = ""

while n >= b:
    m = n % b
    n //= b

    if m < 10:
        a += str(m)
    else:
        a += chr(m + 55)

m = n % b
if m < 10:
    a += str(m)
else:
    a += chr(m + 55)

print(a[::-1])