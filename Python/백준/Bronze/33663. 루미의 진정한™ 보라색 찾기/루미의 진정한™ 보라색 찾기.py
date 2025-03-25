h_lo, h_hi = map(int, input().split())
s_lo, s_hi = map(int, input().split())
v_lo, v_hi = map(int, input().split())
 
r, g, b = map(int, input().split())
v = max(r, g, b)
s = 255 * (v - min(r, g, b)) / v
 
if v == r:
    h = (60 * (g - b)) / (v - min(r, g, b))
elif v == g:
    h = 120 + ((60 * (b - r)) / (v - min(r, g, b)))
else:
    h = 240 + (60 * (r - g) / (v - min(r, g, b)))
 
if h < 0:
    h += 360
 
if h_lo <= h <= h_hi and s_lo <= s <= s_hi and v_lo <= v <= v_hi:
    print("Lumi will like it.")
else:
    print("Lumi will not like it.")
