ans = 0
s = input()

while True:
    try:
        x = input()

        ans += x.count(s)
    except EOFError:
        break


print(ans)
