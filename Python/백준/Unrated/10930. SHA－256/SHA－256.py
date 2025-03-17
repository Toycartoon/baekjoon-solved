import hashlib

sha = hashlib.sha256()
sha.update(input().encode())
print(sha.hexdigest())