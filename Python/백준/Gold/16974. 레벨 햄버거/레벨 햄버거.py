def get_len(l):
    if l == 0:
        return 1
    return get_len(l-1) * 2 + 3


def get_p(l):
    if l == 0:
        return 1
    return 2 * get_p(l-1) + 1


def f(l, p):
    len_h = get_len(l)
    if l == 0:
        return 1

    if p == 1:
        return 0
    elif 1 < p <= (len_h - 3) // 2 + 1:
        return f(l-1, p - 1)
    elif p == (len_h - 3) // 2 + 2:
        return get_p(l-1) + 1
    elif p <= (len_h - 3) + 2:
        return f(l-1, p-2-get_len(l-1)) + get_p(l-1) + 1
    else:
        return get_p(l-1) * 2 + 1


n, x = map(int, input().split())

print(f(n, x))