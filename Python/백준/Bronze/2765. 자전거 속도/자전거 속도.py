t = 1
while True:
    inch, rpm, time = map(float, input().split())

    if rpm == 0:
        break

    dist = inch / 63360 * rpm * 3.1415927
    print("Trip #{}: {:.02f} {:.02f}".format(t, round(dist, 2), round(dist / (time / 3600), 2)))

    t += 1
