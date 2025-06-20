while True:
    d, horizontal, vertical = map(float, input().split())

    if d == horizontal == vertical == 0:
        break

    w = 16 * d / (337) ** 0.5
    h = 9 / 16 * w

    print(f"Horizontal DPI: {horizontal / w:.2f}")
    print(f"Vertical DPI: {vertical / h:.2f}")
