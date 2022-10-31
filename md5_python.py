# Implementing md5 in python
# EXP6

import hashlib

text = input("enter the string: ")
encoded = text.encode()
result = hashlib.md5(encoded)
print("Text ",end="")
print(text)
print("Hash Value ",end="")
print(result)
print("Hexadecimal equivalent: ",result.hexdigest())
