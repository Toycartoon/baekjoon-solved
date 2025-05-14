n = int(input())
s = input()

f = False
v = 0
for i in range(1, n):
    if abs(ord(s[i-1]) - ord(s[i])) == 1:
        if v == 0:
            v = 2
        else:
            v += 1
    else:
        v = 0

    if v >= 5:
        f = True
        break


print("YES" if f else "NO")
