n = int(input())
s = ""
for i in range(2 * n - 1):
    x = input()

    if x == "/":
        x = "//"
    s += x

print(eval(s))
