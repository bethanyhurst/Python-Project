import hashlib
import string

def checkNum(char): #Checks if a given string is a number
    try:
        char = int(char) #Try to convert the string into an integer
        return(True)
    except:
        return(False)

def passwordStrength(password): #Finds the number of each type of character in the given password
    numChar = 0, numLet = 0, numLetUpp = 0, numLetLow = 0, numNum = 0, numSym = 0
    listAlphabet = list(string.ascii_letters)
    listAlphabetLow = list(string.ascii_lowercase)
    listAlphabetUpp = list(string.ascii_uppercase)

    for char in password: #Go through each character in the password
        if(checkNum(char) == True): #If the character is a number
            numNum += 1
        elif(char in listAlphabet): #if the character is a letter
            if(char in listAlphabetLow): #If it is lower case
                numLetLow += 1
            else: #it is upper case
                numLetUpp += 1
            numLet += 1
        else: #It is a symbol
            numSym += 1
        numChar += 1
##    print("number of characters = " + str(numChar))
##    print("number of letters = " + str(numLet))
##    print("number of upper case letters = " + str(numLetUpp))
##    print("number of lower case letters = " + str(numLetLow))
##    print("number of numbers = " + str(numNum))
##    print("number of symbols = " + str(numSym))
    #print(passList)

def passwordVal(userName, password): #Checks that a username and password have been entered
    returnVal = False
    if(userName != "" and password != ""): #If there is no values for the username and password
        returnVal = True
    return(returnVal)

def passwordVer(userName, password): #Checks if the given password is correct for the given username
    returnVal = False

    with open("users.txt") as source:
        userNames = [line.strip().split(', ')[1] for line in source]# Populates a list with the usernames in the file
    with open("users.txt") as source:
        passwords = [line.strip().split(', ')[2] for line in source]# Populates a list with the passwords in the file

    passIndex = userNames.index(userName) #Get the index of the username

    if(passIndex != ValueError): #If the username isn't in the list
        hashedPass = hashlib.md5(password.encode()) #Hash the entered password
        if(passwords[passIndex] == hashedPass.hexdigest()): #Check against stored password
           returnVal = True #The password is right
        else:
            returnVal = False #The password is wrong
    else:
        returnVal = False #The username is not valid

    return(returnVal)

##password = input("Enter pass")
##passwordStrength(password)

##pr = passwordVer("a5623", "SYBOTISM")
##print(pr)