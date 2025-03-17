import base64

s = input().encode()
enc = base64.b16encode(s)
print(enc.decode())
