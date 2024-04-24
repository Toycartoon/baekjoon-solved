while True:
    n = int(input())
    if n == 0:
        break

    reverse_n = []
    for _ in str(n):
        reverse_n.append(_)

    reverse_n = reversed(reverse_n)
    reverse_n = int("".join(reverse_n))
    if reverse_n == n:
        print("yes")
    else:
        print("no")