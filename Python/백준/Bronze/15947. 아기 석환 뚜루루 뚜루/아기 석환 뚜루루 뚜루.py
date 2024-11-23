from math import ceil


w = ["baby", "sukhwan", "turu", "tu", "very", "cute", "turu", "tu", "in", "bed", "turu", "tu", "baby", "sukhwan"]

n = int(input())
i = (n - 1) % 14

if w[i] == "tu" or w[i] == "turu":
    s = w[i] + "ru" * ceil(n / 14)
    if s.count("ru") >= 5:
        print(f"tu+ru*{s.count('ru')}")
    else:
        print(s)
else:
    print(w[i])
