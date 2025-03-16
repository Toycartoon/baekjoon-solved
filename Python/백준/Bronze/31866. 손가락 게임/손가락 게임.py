j, i = map(int, input().split())

if j == 0:
    if i == 5:
        print("<")
    elif i == 0:
        print("=")
    else:
        print(">")
elif j == 2:
    if i == 2:
        print("=")
    elif i == 0:
        print("<")
    else:
        print(">")
elif j == 5:
    if i == 5:
        print("=")
    elif i == 2:
        print("<")
    else:
        print(">")
else:
    if i == 0 or i == 2 or i == 5:
        print("<")
    else:
        print("=")
