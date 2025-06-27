s = input()
a = [0 for _ in range(26)]

for i in s:
    a[ord(i)-97] += 1

s = sorted({*s}, key=lambda x: (-a[ord(x)-97], ord(x)))
[print(i * a[ord(i)-97], end='') for i in s]
