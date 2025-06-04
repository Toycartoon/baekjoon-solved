n = int(input())
s = input()

s = s.replace("..", "  ")
for i in s.split("."):
    if len(i) == 4:
        print("v", end="")
    else:
        print("w", end="")
