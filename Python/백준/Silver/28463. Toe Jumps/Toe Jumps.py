w = input()
g = [input() for _ in range(2)]

t = [["O.", ".P"], ["P.", ".O"], [".O", "P."], [".P", "O."]]
f = [[".P", "I."], [".I", "P."], ["I.", ".P"], ["P.", ".I"]]
lz = [[".P", "O."], [".O", "P."], ["O.", ".P"], ["P.", ".O"]]

arr = {"E": 0, "W": 1, "S": 2, "N": 3}
if t[arr[w]] == g:
    print("T")
elif f[arr[w]] == g:
    print("F")
elif lz[arr[w]] == g:
    print("Lz")
else:
    print("?")
