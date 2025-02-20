n, a, b = map(int, input().split())
s, t = map(int, input().split())

if s > t:
    s, t = t, s

if s >= b or t <= a:
    print("Outside")
elif a < s < b and a < t < b:
    print("City")
else:
    print("Full")