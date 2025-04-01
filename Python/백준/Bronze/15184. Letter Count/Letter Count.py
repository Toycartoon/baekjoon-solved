s = input().upper()
w = [0 for _ in range(26)]

for i in s:
    if i.isalpha():
        w[ord(i)-65] += 1

for i in range(26):
    print(f"{chr(i+65)} | {'*' * w[i]}")
