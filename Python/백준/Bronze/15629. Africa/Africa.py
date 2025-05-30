w = {"botswana": 0, "ethiopia": 50, "kenya": 50, "namibia": 140, "south-africa": 0,
     "tanzania": 50, "zambia": 50, "zimbabwe": 30}

i = []
n = int(input())
for _ in range(n):
    i.append(input())

ans = 0
if "south-africa" in i and "namibia" in i:
    if i.index("south-africa") < i.index("namibia"):
        ans += 40
        w["namibia"] = 0

if "zambia" in i and "zimbabwe" in i:
    if abs(i.index("zambia") - i.index("zimbabwe")) == 1:
        ans += 50
        w["zambia"] = 0
        w["zimbabwe"] = 0

for x in i:
    ans += w[x]

print(ans)
