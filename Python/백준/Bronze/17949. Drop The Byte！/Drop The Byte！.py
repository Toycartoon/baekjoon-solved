p = input()
n = int(input())
l = input().split()

i = 0
s = ""
ans = []
for x in p:
    s += x

    if l[i] == "char" and len(s) == 2:
        ans.append(int(s, 16))
        s = ""
        i += 1
    elif l[i] == "int" and len(s) == 8:
        ans.append(int(s, 16))
        s = ""
        i += 1
    elif l[i] == "long_long" and len(s) == 16:
        ans.append(int(s, 16))
        s = ""
        i += 1


print(*ans)
