import re

ans = ""
p = r"([a-zA-Z-]+)+"

while True:
    s = input()

    for i in re.findall(p, s):
        if i == "E-N-D":
            print(ans.lower())
            exit()

        if len(ans) < len(i):
            ans = i
