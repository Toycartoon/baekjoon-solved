t = int(input())
for _ in range(t):
    ans = input()
    l = []
    total = 0
    for i in range(len(ans)):
        l.append(ans[i])

    for i in range(len(l)):
        if i == 0 and l[i] == "O":
            l[i] = "1"
        elif i == 0 and l[i] == "X":
            l[i] = "0"
        else:
            if l[i] == "O":
                if int(l[i - 1]) != 0:
                    l[i] = str(int(l[i - 1]) + 1)
                else:
                    l[i] = 1
            elif l[i] == "X":
                l[i] = "0"

    for i in l:
        total += int(i)

    print(total)