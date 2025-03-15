import sys

input = sys.stdin.readline

for p in range(int(input())):
    w = {"TTT": 0, "TTH": 0, "THT": 0, "THH": 0, "HTT": 0, "HTH": 0, "HHT": 0, "HHH": 0}
    s = input().strip()

    for i in range(2, len(s)):
        w[s[i-2:i+1]] += 1

    for v in w.values():
        print(v, end=" ")
    print()
