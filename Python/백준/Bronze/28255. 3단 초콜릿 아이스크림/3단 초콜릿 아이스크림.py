from math import ceil

for _ in range(int(input())):
    s = input()
    s_ = s[:ceil(len(s) / 3)]

    if s == s_ + s_[::-1] + s_:
        print(1)
    elif s == s_ + (s_[::-1])[1:] + s_:
        print(1)
    elif s == s_ + s_[::-1] + s_[1:]:
        print(1)
    elif s == s_ + (s_[::-1])[1:] + s_[1:]:
        print(1)
    else:
        print(0)