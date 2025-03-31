while True:
    try:
        a = input()
        b = input()

        ax = [0 for _ in range(26)]
        bx = [0 for _ in range(26)]

        for i in a:
            ax[ord(i)-97] += 1

        for i in b:
            bx[ord(i)-97] += 1

        for i in range(26):
            print(chr(i+97) * min(ax[i], bx[i]), end="")
        print()
    except EOFError:
        break