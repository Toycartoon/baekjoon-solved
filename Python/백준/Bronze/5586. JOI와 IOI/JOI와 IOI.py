s = input()
joi, ioi = 0, 0
for i in range(2, len(s)+1):
    if s[i-3:i] == "JOI":
        joi += 1
    elif s[i-3:i] == "IOI":
        ioi += 1

print(joi)
print(ioi)