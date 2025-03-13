n = int(input())
l = list(map(int, input().split()))
s = input()

f = True
l[ord(s[0])-97] -= 1

for i in range(1, n):
    if s[i-1] == s[i]:
        f = False
        break
    l[ord(s[i])-97] -= 1

for i in l:
    if i < 0:
        f = False
        break

if f and s[0] == s[-1] == "a":
    print("Yes")
else:
    print("No")
