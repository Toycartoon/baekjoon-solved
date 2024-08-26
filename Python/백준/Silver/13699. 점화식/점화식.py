m = {0: 1}
n = int(input())

def dp(i):
    if i in m:
        return m[i]
    
    v = 0
    for x in range(i):
        v += dp(x) * dp(i-x-1)
    m[i] = v
    return m[i]


print(dp(n))