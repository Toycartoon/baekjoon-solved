from math import gcd

ans = 0
x = []
while True:
    try:
        x.extend(list(map(int, input().split())))
    except EOFError:
        break

for i in range(len(x)):
    for j in range(i+1, len(x)):
        ans = max(ans, gcd(x[i], x[j]))

print(ans)