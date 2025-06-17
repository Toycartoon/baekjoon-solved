a = []
for _ in range(5):
    if "FBI" in input():
        a.append(str(_ + 1))

if len(a) == 0:
    print("HE GOT AWAY!")
else:
    print(" ".join(a))