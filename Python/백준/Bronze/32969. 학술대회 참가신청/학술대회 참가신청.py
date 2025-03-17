s = input().split()

for i in s:
    if i in ["history", "social", "language", "literacy"]:
        print("digital humanities")
        break
    elif i in ["bigdata", "public", "society"]:
        print("public bigdata")
        break
