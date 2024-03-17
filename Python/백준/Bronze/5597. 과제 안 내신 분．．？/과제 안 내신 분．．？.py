s = [0 for _ in range(30)]

for i in range(28):
    n = int(input())
    s[n - 1] = 1
    
for i in range(len(s)):
    if s[i] == 0:
        print(i + 1)