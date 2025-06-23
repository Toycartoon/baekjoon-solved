t = int(input())
s = int(input())
h = int(input())

for i in range(t):
    print(("*" + " " * s) * 2 + "*")
print("*" * (3 + 2 * s))
for i in range(h):
    print(" " * (s+1) + "*")
