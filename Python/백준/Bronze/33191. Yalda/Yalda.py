h = int(input())
w = int(input())
p = int(input())
n = int(input())

if h >= w:
    print("Watermelon")
elif h >= p:
    print("Pomegranates")
elif h >= n:
    print("Nuts")
else:
    print("Nothing")
