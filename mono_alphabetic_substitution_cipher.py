# Implement mono alphabetic substitution cipher
# EXP3
plaintext = input("Enter the text: ")
abc = "abcdefghijklmnopqrstuvwxyz"
encrypt = "".join([abc[(abc.find(c) + 13)%26] for c in plaintext])
decrypt = "".join([abc[(abc.find(c) + 13)%26] for c in encrypt])

print("The original text is " + plaintext)
print("The encrypted text is " + encrypt)
print("The decrypted text is " + decrypt)