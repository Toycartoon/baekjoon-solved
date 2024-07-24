from itertools import combinations as comb

l, c = map(int, input().split())
a = list(input().split())

temp = sorted(list(comb(a, l)))
ans = set()
for v in temp:
    if len(set(("a", "e", "i", "o", "u")) - set(v)) == 5 or len(set(v) - set(("a", "e", "i", "o", "u"))) < 2:
        continue
    x = sorted(list(v))
    ans.add("".join(x))

for i in sorted(list(ans)):
    print(i)
