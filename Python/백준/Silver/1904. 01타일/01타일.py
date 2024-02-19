m = [0] * 1000001
m[1] = 1
m[2] = 2
m[3] = 3

n = int(input())
for i in range(4, n + 1):
    m[i] = (m[i - 2] + m[i - 1]) % 15746

print(m[n])
