s = input()
z = s.count("0") // 2
o = s.count("1") // 2

for i in s:
    if i == "0":
        if z > 0:
            z -= 1
            print("0", end="")
    else:
        if o > 0:
            o -= 1
        else:
            print("1", end="")
