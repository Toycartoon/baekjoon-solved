n, m = map(int, input().split())
p = 1000000007
print((pow(m, n, p) - pow(m-1, n, p)) % p)