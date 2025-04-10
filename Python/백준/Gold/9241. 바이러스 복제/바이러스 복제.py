a = input()
b = input()

s, e = -1, -1
for i in range(min(len(a), len(b))):
    if a[i] != b[i]:
        s = i
        break

for i in range(min(len(a), len(b))):
    if a[-i-1] != b[-i-1]:
        e = len(b) - i
        break

if s == -1 or e == -1:
    if len(a) >= len(b):
        print(0)
    else:
        print(len(b)-len(a))
else:
    if e < s:
        print(0)
    else:
        print(e-s)
