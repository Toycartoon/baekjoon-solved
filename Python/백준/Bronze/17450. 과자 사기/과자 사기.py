s = list(map(int, input().split()))
n = list(map(int, input().split()))
u = list(map(int, input().split()))

s = s[1] * 10 / (s[0] * 10 - (500 if s[0] * 10 >= 5000 else 0))
n = n[1] * 10 / (n[0] * 10 - (500 if n[0] * 10 >= 5000 else 0))
u = u[1] * 10 / (u[0] * 10 - (500 if u[0] * 10 >= 5000 else 0))

if max(s, n, u) == s:
    print("S")
elif max(s, n, u) == n:
    print("N")
else:
    print("U")
