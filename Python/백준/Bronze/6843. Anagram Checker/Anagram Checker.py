a = input()
b = input()

x = [0 for _ in range(26)]
for i in a:
    if i.isalpha():
        x[ord(i)-65] += 1

for i in b:
    if i.isalpha():
        x[ord(i)-65] -= 1

f = True
for i in x:
    if i != 0:
        f = False
        break

if f:
    print("Is an anagram.")
else:
    print("Is not an anagram.")
