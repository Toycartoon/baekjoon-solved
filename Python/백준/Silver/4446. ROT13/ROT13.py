v = ("a", "i", "y", "e", "o", "u")
c = ("b", "k", "x", "z", "n", "h", "d", "c", "w", "g", "p", "v", "j", "q", "t", "s", "r", "l", "m", "f")

while True:
    try:
        s = input()

        ans = ""
        for w in s:
            if w.isalpha():
                if w.lower() in v:
                    ans += v[v.index(w.lower()) - 3].upper() if w.isupper() else v[v.index(w.lower()) - 3]
                else:
                    ans += c[c.index(w.lower()) - 10].upper() if w.isupper() else c[c.index(w.lower()) - 10]
            else:
                ans += w

        print(ans)
    except EOFError:
        break