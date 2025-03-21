s = [*input()]
ans = ["U", "A", "P", "C"]

for i in s:
    ans.remove(i)

print("".join(ans))
