n = int(input())

for k in range(n, -1, -1):
    if k == 1:
        x = "1 bottle"
        y = "no more bottles"
    elif k == 0:
        x = "No more bottles"
        y = f"Go to the store and buy some more, {str(n) + ' bottles' if n > 1 else '1 bottle'} of beer on the wall."
    else:
        x = str(k) + " bottles"
        if k == 2:
            y = "1 bottle"
        else:
            y = str(k-1) + " bottles"

    print(f"{x} of beer on the wall, {x.lower()} of beer.")
    print(y if k == 0 else f"Take one down and pass it around, {y} of beer on the wall.")
    print()