for t in range(int(input())):
    s = input()
    if s[-1].lower() == "y":
        v = "nobody"
    elif s[-1].lower() in "aeiou":
        v = "a queen"
    else:
        v = "a king"

    print(f"Case #{t+1}: {s} is ruled by {v}.")
