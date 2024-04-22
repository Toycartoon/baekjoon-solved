while True:
    usable_k = int(input())
    if usable_k == 0:
        break
    sentence = input()
    ascii_k = [0] * 128
    max_length = 0

    l, r = -1, -1
    using_k = 0
    while l <= r:
        if usable_k > using_k or (using_k == usable_k and ascii_k[ord(sentence[r + 1])] > 0):
            r += 1
            if ascii_k[ord(sentence[r])] == 0:
                using_k += 1
            ascii_k[ord(sentence[r])] += 1
        else:
            l += 1
            ascii_k[ord(sentence[l])] -= 1
            if ascii_k[ord(sentence[l])] == 0:
                using_k -= 1

        max_length = max(r - l, max_length)

        if r == len(sentence) - 1:
            break

    print(max_length)