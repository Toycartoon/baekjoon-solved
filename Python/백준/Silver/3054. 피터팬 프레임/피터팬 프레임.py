s = input()
g = [[], [], [], [], []]

for x in range(len(s)):
    i = s[x]
    if (x+1) % 3 == 0:
        g[0].append("..*..")
        g[1].append(".*.*.")
        g[2].append(f"*.{i}.*")
        g[3].append(".*.*.")
        g[4].append("..*..")
    else:
        if x == 0 or x % 3 != 0:
            g[0].append(".")
            g[1].append(".")
            g[2].append("#")
            g[3].append(".")
            g[4].append(".")
        g[0].append(".#.")
        g[1].append("#.#")
        g[2].append(f".{i}.")
        g[3].append("#.#")
        g[4].append(".#.")
        if x == len(s)-1:
            g[0].append(".")
            g[1].append(".")
            g[2].append("#")
            g[3].append(".")
            g[4].append(".")


for x in g:
    print("".join(x))
