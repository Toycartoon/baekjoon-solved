w = [13, 7, 5, 3, 3, 2]

c = list(map(int, input().split()))
h = list(map(int, input().split()))

chu = 0
han = 0

for i in range(6):
    chu += c[i] * w[i]
    han += h[i] * w[i]

han += 1.5
if han > chu:
    print("ekwoo")
else:
    print("cocjr0208")
