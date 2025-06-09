from math import factorial as f
import sys

input = sys.stdin.readline

for i in range(int(input())):
    s, n, t, l = input().split()

    n, t, l = int(n), int(t), int(l)
    match s:
        case "O(N)":
            if n * t <= l * (10 ** 8):
                print("May Pass.")
            else:
                print("TLE!")
        case "O(2^N)":
            if pow(2, n) * t <= l * (10 ** 8):
                print("May Pass.")
            else:
                print("TLE!")
        case "O(N!)":
            if f(n) * t <= l * (10 ** 8):
                print("May Pass.")
            else:
                print("TLE!")
        case "O(N^2)":
            if n ** 2 * t <= l * (10 ** 8):
                print("May Pass.")
            else:
                print("TLE!")
        case "O(N^3)":
            if n ** 3 * t <= l * (10 ** 8):
                print("May Pass.")
            else:
                print("TLE!")
