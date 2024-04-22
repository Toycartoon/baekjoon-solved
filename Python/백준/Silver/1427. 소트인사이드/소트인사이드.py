n = list(map(int, list(input())))
n.sort(reverse=True)
print("".join(list(map(str, n))))