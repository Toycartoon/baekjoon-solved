word = {"@": "a", "[": "c", "!": "i", ";": "j", "^": "n", "0": "o", "7": "t"}
for t in range(int(input())):
    s = input()
    ans = ""
    x = 0
    w = 0
    for i in range(len(s)):
        if i + w >= len(s):
            break

        if s[i+w] in word:
            ans += word[s[i+w]]
            x += 1
        elif s[i+w] == "\\":
            if s[i+w:i+w+3] == "\\\\\'":
                w += 2
                ans += "w"
                x += 1
            elif s[i+w+1] == "\'":
                w += 1
                ans += "v"
                x += 1
        else:
            ans += s[i+w]


    if x >= len(ans) / 2:
        print("I don't understand")
    else:
        print(ans)
