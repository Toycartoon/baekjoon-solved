for t in range(int(input())):
    s = input()
    ans = 0
    for i in s:
        if i in "aeiou":
            ans += 1

    print(f"The number of vowels in {s} is {ans}.")
