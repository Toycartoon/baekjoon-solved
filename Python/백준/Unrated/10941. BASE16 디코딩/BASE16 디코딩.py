import base64

s = input().encode()
dec = base64.b16decode(s)
print(dec.decode())
