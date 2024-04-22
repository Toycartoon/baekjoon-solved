s = input()
a = 0

l = set()
for i in range(1, len(s)):
    for j in range(len(s)):
        l.add(s[j:j+i])


print(len(l)+1)