from math import floor

s = input()
a = ""
op = ""
b = ""
for i in range(len(s)):
    if s[i] in "+-/*" and i != 0 and op == "":
        op = s[i]
    elif op != "":
        b += s[i]
    else:
        a += s[i]

try:
    ans = oct(floor((eval(str(int(a, 8))+op+str(int(b, 8))))))
    if ans[0] == "-":
        print("-" + ans[3:])
    else:
        print(ans[2:])
except:
    print("invalid")
