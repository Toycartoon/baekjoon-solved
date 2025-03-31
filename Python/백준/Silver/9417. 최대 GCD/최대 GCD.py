from math import gcd

for n in range(int(input())):
    m = list(map(int, input().split()))

    ans = 0
    for i in range(len(m)):
        for j in range(i+1, len(m)):
            ans = max(ans, gcd(m[i], m[j]))

    print(ans)
