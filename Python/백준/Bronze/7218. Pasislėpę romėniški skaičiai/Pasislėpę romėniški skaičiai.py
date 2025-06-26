n = int(input())
s = input()

w = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]
for i in range(len(w)):
    if w[i] in s:
        print(i+1, end=" ")
