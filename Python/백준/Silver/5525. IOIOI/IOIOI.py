n = int(input())
m = int(input())
s = input()

ans = 0
i = 0
while i < m:
    if s[i] == "I":
        j = 1
        a = 0
        while True:
            if s[i+j:i+j+2] == "OI":
                a += 1
            else:
                ans += max(a - n + 1, 0)
                break
            j += 2
        i += j - 1

    i += 1

print(ans)