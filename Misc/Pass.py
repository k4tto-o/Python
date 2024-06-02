import random

possible = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pssword = ""
qst = int(input("Cantidad de caracteres:"))
for i in range (qst):
    rndm = random.choice(possible)
    pssword += rndm

print(pssword)