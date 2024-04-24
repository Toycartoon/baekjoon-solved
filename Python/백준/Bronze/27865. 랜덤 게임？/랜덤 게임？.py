import sys, random

l = list(range(1, int(input())+1))

while True:
    x = random.choice(l)
    print(f"? {x}")
    sys.stdout.flush()

    a = input()
    if a == "Y":
        print(f"! {x}")
        sys.stdout.flush()
        break