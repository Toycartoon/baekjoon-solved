ans = ""
mx = 201
while True:
    try:
        s, t = input().split()

        if mx > int(t):
            ans = s
            mx = int(t)
    except EOFError:
        print(ans)
        break
