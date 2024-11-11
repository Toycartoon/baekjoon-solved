w = [0 for _ in range(26)]
while True:
    try:
        s = input()

        for i in s:
            if i.isalpha():
                w[ord(i)-ord('a')]+=1
    except EOFError:
        break

m = max(w)
for i in range(26):
    if w[i] == m:
        print(chr(i+ord('a')), end='')
