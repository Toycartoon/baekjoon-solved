n = int(input())
cards = [i for i in range(1, n + 1)]

trash = []
while True:
    try:
        trash.append(str(cards.pop(0)))
        cards.append(cards.pop(0))
    except IndexError:
        break

print(" ".join(trash))