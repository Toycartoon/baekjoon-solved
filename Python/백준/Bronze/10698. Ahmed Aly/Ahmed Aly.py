for t in range(int(input())):
    s = input().replace("=", "==")
    print(f"Case {t+1}: {'YES' if eval(s) else 'NO'}")
