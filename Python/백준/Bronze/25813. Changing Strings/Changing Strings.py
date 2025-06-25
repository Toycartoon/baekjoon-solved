s = input()
u = s.index("U")
f = len(s) - s[::-1].index("F") - 1

for i in range(u):
    print("-", end="")
print("U", end="")
for i in range(u+1, f):
    print("C", end="")
print("F", end="")
for i in range(f+1, len(s)):
    print("-", end="")
