w = {1: "Yakk", 2: "Doh", 3: "Seh", 4: "Ghar", 5: "Bang", 6: "Sheesh"}

for t in range(int(input())):
    a, b = map(int, input().split())

    if a == b:
        print(f"Case {t+1}: " + ["Habb Yakk", "Dobara", "Dousa", "Dorgy", "Dabash", "Dosh"][a-1])
        continue
    if sorted((a, b)) == [5, 6]:
        print(f"Case {t+1}: Sheesh Beesh")
    else:
        print(f"Case {t+1}:", end=" ")
        for i in sorted((a, b), reverse=True):
            print(w[i], end=" ")
        print()
