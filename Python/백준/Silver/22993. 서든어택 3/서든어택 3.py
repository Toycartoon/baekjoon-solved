n = int(input())
a = list(map(int, input().split()))
j = a[0]
a = a[1:]

a.sort()
f = True
for atk in a:
    if atk >= j:
        f = False
    else:
        j += atk

if f:
    print("Yes")
else:
    print("No")