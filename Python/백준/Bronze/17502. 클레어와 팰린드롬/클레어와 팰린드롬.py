n = int(input())
s = [*input()]

for i in range(n):
    if s[i] == "?":
        if s[n-i-1] != "?":
            s[i] = s[n-i-1]
        else:
            s[i] = "a"
            s[n-i-1] = "a"


print("".join(s))
