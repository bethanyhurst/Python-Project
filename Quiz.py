##add a function to choose between encrypt or decrypt and generate a word

import string
import random #####

def checkAnswer(message, codedMessage, decrypt): ####checks all answers
    score = 0
    numOfAttempts = 3
    while numOfAttempts> 0:
        response = input("type your answer, you have " + str(numOfAttempts) + " attempts left")####
        if ((decrypt == True and response == message) or (decrypt == False and response == codedMessage)): ####
            print("Well done!")
            score += 1
            break
        else:
            print("Incorrect! Try again.")
            numOfAttempts -= 1
    if (numOfAttempts <= 0):
        print("Too many wrong answers")
        ####Next question

def caesar():
    alphabet = string.ascii_lowercase ####
    alphLen = len(alphabet) ####
    message = "hello" ####Placeholder for word generated
    question = "this message, " + message
    shift = random.randint(0, 25) #Choose a shift
    decrypt = random.choice([True, False]) #Choose encode or decode

    if decrypt == False: #Encode
        shift = shift
        question = "Encrypt this message, using the caesar cipher, shift " + str(shift) + ": " +message ####
    else: ####Decode
        shift *= -1 ####
        question = "Decrypt this message, using the caesar cipher, shift " + str(shift) ####

    codedMessage = []

    for char in message:
        if char in alphabet:
            charPos = alphabet.index(char)
        newCharPos = (charPos + shift) % alphLen
        codedMessage.append(alphabet[newCharPos])

    if decrypt == True:
        question += ": " + "".join(codedMessage)

    print(question)
    print(message) ####Shows answers
    print("".join(codedMessage)) ####
    checkAnswer(message, "".join(codedMessage), decrypt) ####

def vigenereTable(): #Function to fill a list with lists of the alphabet with different shifts
    table = []
    for i in range(25): #Make the table have 26 items
        table.append([])

    for row in range(25): #Foor each letter in the alphabet
        for column in range(26):
            if (row + 65) + column > 90:
                # moving back to A after Z
                # after first row, each letter will shift left by one position compared to row above it
                table[row].append(chr((row+65) + column - 26)) #Add the letter to the table
            else:
                # after first row, each letter will shift left by one position compared to row above it
                character = chr((row+65)+column)
                table[row].append(character) #Add the letter to the table
    return table


def vigenereEncryption(message, mappedKey):
    table = vigenereTable() #Get a table of all the shifted alphabets
    codedMessage = ""

    for i in range(len(message)): #For each character in the message
        if message[i] == chr(32): #If the character is a space
            # ignoring space
            codedMessage += " " #Add a space to the ciphertext
        else:
            # getting element at specific index of table
            row = ord(message[i])-65 #The row in the table of the encoded character
            column = ord(mappedKey[i]) - 65 #The column in the table
            codedMessage += table[row][column] #Add the encoded character to the ciphertext
    print(codedMessage) ####Show answer
    return(codedMessage)

def vigenereMessageKey():
    msg = "hello".upper() ##Placeholder for message generation
    key = "key".upper() ##Placeholder for key generation
    # variable to store mapped key
    keyMap = "" #The key repeated for the same number of characters as the message
    j=0 #Holds the place of the current key character

    for i in range(len(msg)): #Counts through each letter in the message
        if ord(msg[i]) == 32: #ord() gets the unicode code for the character
            #If the current letter is a space
            keyMap += " " #A space lined up with each space in the message
        else:
            if j < len(key): #Count through the letters in the key
                keyMap += key[j] #Add the character to the key map
                j += 1 #Move to next letter
            else:
                j = 0 #Go back to the start of the key
                keyMap += key[j] #Add the character to the key map
                j += 1 #Move to next letter

    #print(keyMap)
    return msg, keyMap, key #Return the obtained values

def vigenere(): #Vigenere question
    decrypt = random.choice([True, False]) #Choose encode or decode
    message, mappedKey, key = vigenereMessageKey() #Get the message and the key
    codedMessage = vigenereEncryption(message, mappedKey) #Encrypt the message
    if decrypt == False: #Encrypt
        print("Encrypt the following message, using the vigenere cipher with " + key + " as the key: " + message)

    else: #Decrypt
        print("Decrypt the following message, using the vigenere cipher with " + key + " as the key: " + codedMessage)
    checkAnswer(message, codedMessage,decrypt)

def fencepost():
    fencePostHeight = random.randit(0, 10)
    decrypt = random.choice([True, False]) #Choose encode or decode
    msg = "hello".upper()
    encodedMessage = ""
    for k in range(fenceHeight):
        encodedMessage += messageToEncode[k: : fenceHeight]


    if decrypt == False: #Encrypt
        print("Encrypt the following message, using the fence post cipher: " + msg )

    else:
        print("Decrypt the following message, using the fence post cipher: " + encodedMessage )

fencepost()
