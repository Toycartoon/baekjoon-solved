from itertools import permutations as p

x = input()
ans = int(x)

for i in p(sorted([*x]), len(x)):
    a = int("".join(i))
    if a > ans:
        ans = a
        break

if ans == int(x):
    print(0)
else:
    print(ans)
