n = int(input())
a = input()
b = input()

f = True
if n % 2 == 0:
    if a != b:
        f = False
else:
    for i in range(len(a)):
        if a[i] == b[i]:
            f = False
            break


if f:
    print("Deletion succeeded")
else:
    print("Deletion failed")
