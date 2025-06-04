a = input()
b = input()

new_a = ""
new_b = ""

v = False
for i in range(1, len(a)):
    if a[i-1] in "aeiou" and a[i] not in "aeiou":
        new_a += a[i-1]
        v = True
        break
    else:
        new_a += a[i-1]

if not v:
    print("no such exercise")
    exit()

v = False
for i in range(1, len(b)):
    if b[i-1] in "aeiou" and b[i] not in "aeiou":
        new_b += b[i-1]
        v = True
        break
    else:
        new_b += b[i-1]

if not v:
    print("no such exercise")
    exit()

print(new_a+new_b)
