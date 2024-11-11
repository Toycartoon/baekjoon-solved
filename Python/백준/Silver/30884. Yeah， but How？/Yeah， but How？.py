s = input()
t = s.replace("()", "(1)").replace(")(", ")+(")
print(t)