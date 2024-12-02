r, c = map(int, input().split())
f = [list(map(int, input().split())) for _ in range(c)]
g = [list(map(int, input().split())) for _ in range(r)]

h = []
for i in range(r):
    s = []
    for j in range(c-1, -1, -1):
        s.append(f[j][i])

    h.append(s)

if h == g:
    print('''|>___/|        /}
| O < |       / }
(==0==)------/ }
| ^  _____    |
|_|_/     ||__|
''')
else:
    print('''|>___/|     /}
| O O |    / }
( =0= )\"\"\"\"  \\
| ^  ____    |
|_|_/    ||__|
        '''
    )