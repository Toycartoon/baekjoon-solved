while True:
    n = int(input())
    if n == -1:
        break

    s = []
    t = []
    for i in range(1, n):
        if n % i == 0:
            s.append(i)
            t.append(str(i))

    if sum(s) == n:
        print(f"{n} = {' + '.join(t)}")
    else:
        print(f"{n} is NOT perfect.")