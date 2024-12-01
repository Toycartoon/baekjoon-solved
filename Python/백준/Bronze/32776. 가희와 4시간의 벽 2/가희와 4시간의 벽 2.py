sab = int(input())
f = list(map(int, input().split()))

if sum(f) >= sab or sab <= 240:
    print("high speed rail")
else:
    print("flight")