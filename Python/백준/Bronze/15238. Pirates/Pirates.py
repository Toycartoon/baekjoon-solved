n = int(input())
w = [0 for _ in range(26)]
for i in input():
    w[ord(i)-97] += 1

print(chr(w.index(max(w)) + 97), max(w))
