n = int(input())
c = list(map(int, input().split()))
m = int(input())
f = list(map(int, input().split()))
card = {}

for i in c:
    if i in card:
        card[i] += 1
    else:
        card[i] = 1

for j in f:
    if j in card:
        print(card[j], end=" ")
    else:
        print(0, end=" ")