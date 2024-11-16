w = {"Tiger": 0, "Lion": 0}

for i in range(9):
    w[input()] += 1


if w["Tiger"] > w["Lion"]:
    print("Tiger")
else:
    print("Lion")
