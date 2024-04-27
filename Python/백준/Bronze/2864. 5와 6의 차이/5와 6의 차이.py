a, b = input().split()

mia = ""
mib = ""
mxa = ""
mxb = ""

for i in a:
    if i == "5" or i == "6":
        mia += "5"
        mxa += "6"
    else:
        mia += i
        mxa += i

for i in b:
    if i == "5" or i == "6":
        mib += "5"
        mxb += "6"
    else:
        mib += i
        mxb += i

print(f"{int(mia) + int(mib)} {int(mxa) + int(mxb)}")