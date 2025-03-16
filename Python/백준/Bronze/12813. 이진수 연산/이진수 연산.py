sa = input()
sb = input()

a = int(sa, 2)
b = int(sb, 2)

print(bin(a & b)[2:].zfill(100000))
print(bin(a | b)[2:].zfill(100000))
print(bin(a ^ b)[2:].zfill(100000))
not_a = "0" * (100000 - len(sa)) + sa
not_b = "0" * (100000 - len(sb)) + sb
for i in not_a:
    if i == "0":
        print("1", end="")
    elif i == "1":
        print("0", end="")
print()

for i in not_b:
    if i == "0":
        print("1", end="")
    elif i == "1":
        print("0", end="")
print()