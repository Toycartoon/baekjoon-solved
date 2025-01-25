n, m = map(int, input().split())

if (n-1) % (1+m) == 0:
    print("Can't win")
else:
    print("Can win")