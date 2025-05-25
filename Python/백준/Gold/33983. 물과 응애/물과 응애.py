n = int(input())
s = input()

if n % 3 != 0:
    print("mix")
    exit()

f = True
q, o = 0, 0
for i in s:
    if i == "O":
        q -= 1
        o += 1
    else:
        q += 1

    if q < 0:
        f = False
        break

if q != o:
    f = False

q = 0
s = reversed(s)
for i in s:
    if i == "O":
        q -= 1
    else:
        q += 1

    if q < 0:
        f = False
        break

if f and q == o:
    print("pure")
else:
    print("mix")
