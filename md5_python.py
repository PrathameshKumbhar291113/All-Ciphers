# Implementing md5 in python

import hashlib

text = input("enter the string: ")
encoded = text.encode()
result = hashlib.md5(encoded)
print("Text ",end="")
print(text)
print("Hash Value ",end="")
print(result)
print("Hexadecimal equivalent: ",result.hexdigest())
