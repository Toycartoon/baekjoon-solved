while True:
    s = input()

    if s == "EOI":
        break

    if "NEMO" in s.upper():
        print("Found")
    else:
        print("Missing")
