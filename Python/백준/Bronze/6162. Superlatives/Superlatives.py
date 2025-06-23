for n in range(int(input())):
    e, a = map(int, input().split())

    print(f"Data Set {n+1}:")
    if e <= a:
        print("no drought\n")
        continue

    s = "drought"
    x = e / a
    while x > 5:
        s = "mega " + s
        x /= 5

    print(s + "\n")
