import sys

s = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

stack = []
a = 0
for i in range(len(s)):
    stack.append(s[i])
    if "".join(stack[i + 1 - len(b) - a:]) == b:
        for j in range(len(b)):
            stack.pop()
            a += 1

if len(stack) == 0:
    sys.stdout.write("FRULA")
else:
    sys.stdout.write("".join(stack))