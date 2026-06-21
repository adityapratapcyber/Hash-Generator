import hashlib

text = input("Enter Text: ")

hash_value = hashlib.sha256(text.encode())

print("SHA256 Hash:")
print(hash_value.hexdigest())
