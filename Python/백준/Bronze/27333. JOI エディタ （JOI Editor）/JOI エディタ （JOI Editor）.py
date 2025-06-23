n = int(input())
s = [*input()]

for i in range(1, n):
    if s[i-1] == s[i]:
        s[i-1] = s[i-1].upper()
        s[i] = s[i].upper()

print(*s, sep="")
