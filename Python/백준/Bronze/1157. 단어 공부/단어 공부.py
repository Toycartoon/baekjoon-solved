n = input().upper()
alphabets = [0 for _ in range(26)]

for i in n:
    alphabets[ord(i) - 65] += 1

big_alphabet = 0
index = 0
flag = True
for j in range(len(alphabets)):
    if alphabets[j] > big_alphabet:
        big_alphabet = alphabets[j]
        index = j
        flag = True
    elif alphabets[j] == big_alphabet:
        if alphabets[j] != 0:
            flag = False

if flag is False:
    print("?")
else:
    print(chr(index + 65))