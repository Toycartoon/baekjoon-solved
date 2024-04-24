n = int(input())

c = 0
s = ""
while c < n:
    i = input()
    if i == "":
        c += 1
        print("Efficiency ratio is %g%%." %(round(100 - s.count("#") / len(s) * 100, 1)))
        s = ""
    else:
        s += i