s = input()
x = "".join(sorted(list(set([*s]))))
print(len(s)-len(x))
