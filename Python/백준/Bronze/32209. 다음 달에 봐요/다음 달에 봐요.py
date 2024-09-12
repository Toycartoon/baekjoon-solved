a = 0
for q in range(int(input())):
    com, x = map(int, input().split())

    if com == 1:
        a += x
    elif com == 2:
        if a >= x:
            a -= x
        else:
            print("Adios")
            exit()


print("See you next month")
