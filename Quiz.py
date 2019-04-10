import random
import string

def caesar():
    shift = random.randint(0, 25) #Choose a shift
    generateQuestion = random.randint(0, 1) #Choose encode or decode
    alphabet = list(string.ascii_uppercase) #Put the alphabet into a list
    if generateQuestion == 0: #Encode
        
    else: #Decode

for k in range(0, 11): #Choose a cipher
    number = random.randint(0, 1)
    if number == 0: #Caesar chosen
        caesar()
