from math import ceil

_min, _max = map(int, input().split())
arr = [i for i in range(_min, _max + 1)]

ans = _max - _min + 1
x = 2
while x ** 2 <= _max:
    i = ceil(_min / x ** 2)
    while x ** 2 * i <= _max:
        if arr[x**2*i-_min] != 0:
            arr[x**2*i-_min] = 0
            ans -= 1
        i += 1

    x += 1


print(ans)
