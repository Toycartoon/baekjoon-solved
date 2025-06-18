g = {"northlondo": "NLCS", "branksomeh": "BHA", "koreainter": "KIS", "stjohnsbur": "SJA"}

s = input()
while True:
    if s in g:
        print(g[s])
        break

    new_s = ""
    for x in s:
        new_s += chr(ord(x)-1) if ord(x) - 1 >= 97 else "z"
    s = new_s
