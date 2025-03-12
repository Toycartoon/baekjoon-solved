n = int(input())
a = input()
b = input()

aw = [0 for _ in range(26)]
bw = [0 for _ in range(26)]
an = ""
bn = ""
for i in a:
    aw[ord(i)-97] += 1

    if i not in "aeiou":
        an += i

for i in b:
    bw[ord(i)-97] += 1

    if i not in "aeiou":
        bn += i

if aw == bw and a[0] == b[0] and a[-1] == b[-1] and an == bn:
    print("YES")
else:
    print("NO")