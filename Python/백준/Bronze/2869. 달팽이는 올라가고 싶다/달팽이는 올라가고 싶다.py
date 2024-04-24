import sys
import math

a, b, v = map(int, sys.stdin.readline().split())

day = 1
v -= a
day += math.ceil(v / (a - b))

sys.stdout.write(str(day))