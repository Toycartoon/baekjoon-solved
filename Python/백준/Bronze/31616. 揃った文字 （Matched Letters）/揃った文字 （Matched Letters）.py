n = int(input())
s = input()

f = True
for i in range(1, n):
    if s[i-1] != s[i]:
        f = False

if f:
    print("Yes")
else:
    print("No")
