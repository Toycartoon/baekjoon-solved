n, m = map(int, input().split())

f = True
for i in range(n):
    if input().count("A") != 1:
        f = False
        break


if f:
    print("Yes")
else:
    print("No")
