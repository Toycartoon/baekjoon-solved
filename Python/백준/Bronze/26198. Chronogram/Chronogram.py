w = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
for t in range(int(input())):
    ans = 0
    s = input()

    for i in s:
        if i in w:
            ans += w[i]

    print(ans)
