while True:
    try:
        n = int(input())

        dp = 0
        for i in range(n+1):
            if i % 2 == 0:
                dp = dp * 2 + 1
            else:
                dp = dp * 2 - 1

        print(dp)
    except EOFError:
        break
