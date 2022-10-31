# Railfence cipher
# EXP5

message = input("Enter message: ")
key = int(input("Enter key: "))
enc = [[" " for i in range(len(message))] for j in range(key)]
flag = 0
row = 0
for i in range(len(message)):
    enc[row][i] = message[i]
    if row == 0:
        flag = 0
    elif row == key - 1:
        flag = 1
    if flag == 0:
        row += 1
    else:
        row -= 1
    ct = []
for i in range(key):
    for j in range(len(message)):
        if enc[i][j] != ' ':
            ct.append(enc[i][j])
    cipher = "".join(ct)
print("Cipher Text: ", cipher)


def decryptRailFence(cipher, key):
    rail = [['\n' for i in range(len(cipher))]
            for j in range(key)]

    dir_down = None
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        rail[row][col] = '*'
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
                    (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(cipher)):

        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        # place the marker
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1

        if dir_down:
            row += 1
        else:
            row -= 1
    return "".join(result)

print("Decrypt message is:")
print(decryptRailFence(cipher, key))
