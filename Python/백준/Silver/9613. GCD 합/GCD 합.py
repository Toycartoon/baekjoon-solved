from math import gcd

for t in range(int(input())):
    n, *m = map(int, input().split())

    ans = 0
    for i in range(len(m)):
        for j in range(i+1, len(m)):
            ans += gcd(m[i], m[j])

    print(ans)
