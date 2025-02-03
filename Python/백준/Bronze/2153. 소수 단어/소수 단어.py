s = input()

x = 0
for i in s:
    if i.isupper():
        x += ord(i) - 38
    elif i.islower():
        x += ord(i) - 96


f = True
for i in range(2, int(x ** 0.5) + 1):
    if x % i == 0:
        f = False
        break


if f:
    print("It is a prime word.")
else:
    print("It is not a prime word.")