for t in range(int(input())):
    s = input()
    if s[-1] == "y":
        v = "nobody"
    elif s[-1] in "aeiou":
        v = "a queen"
    else:
        v = "a king"

    print(f"Case #{t+1}: {s} is ruled by {v}.")
