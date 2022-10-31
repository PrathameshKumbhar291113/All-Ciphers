k = [3,1,4,5,2]
ki = [2,5,1,3,4]
kc = 3
alpha = 'abcdefghijklmnopqrstuvwxyz'
msg = input("Enter the message: ")
msg = "".join(msg.split())
enc = ""
dec = ""
while len(msg)%5 != 0 :
 msg = msg + "x"
for i in msg :
 enc = enc + alpha[(alpha.find(i)+kc)%26]
print("After encryption with CaesarCipher:",enc)
msg = enc
enc = ""
mat = [["x" for i in range(5)] for j in range(int(len(msg)/5))]
print("Transposition Matrix: ")
for i in range(int(len(msg)/5)) :
 for j in range(5):
  print(msg[i*5+j], end=" ")
print()
for i in range(5) :
 for j in range(int(len(msg)/5)) :
  if j*5+k[i]-1 < len(msg) :
   mat[j][i] = msg[j*5+k[i]-1]
enc = ""
for i in range(5) :
 for j in range(int(len(msg)/5)) :
  enc = enc + mat[j][i]
print("Final Encrypted Message:", enc.upper())