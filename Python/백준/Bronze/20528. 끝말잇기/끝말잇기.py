n = int(input())
s = input().split()
x = s[0][0]

f = True
for i in s:
    if i[0] != x:
        f = False
        break

print(int(f))
