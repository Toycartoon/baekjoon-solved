from itertools import product as p


n, k = map(int, input().split())
ans = 0

for i in p(["0", "1"], repeat=n):
    if "".join(i).count("0" * (k + 1)) >= 1 or "".join(i).count("1" * (k + 1)) >= 1:
        continue
    ans += 1


print(ans)
