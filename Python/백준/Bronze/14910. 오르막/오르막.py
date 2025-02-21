a = list(map(int, input().split()))

if sorted(a) == a:
    print("Good")
else:
    print("Bad")
