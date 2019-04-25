#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Bethany
#
# Created:     01/04/2019
# Copyright:   (c) Bethany 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#https://stackoverflow.com/questions/22899536/hangman-code-python3
#Hangman game
import random
with open (words.txt) as source: #words.txt is where the dictionary of words is stored
    WORDLIST = (words.txt)  #wordlist will select and store words from dictionary file
    WORD = random.choice(WORDLIST)  #the words will be selected at random
    ACCEPTABLE = ("abcdefghijklmnopqrstuvwxyz")
    guessed = [] #used words go in here so that they din't get pushed out again
    state = 0
    hasWon = 0
    playedOnce = 0

def menu ():        #Select Difficulty Menu
    print("""
    1. Easy (9 misses)
    2. Medium (7 misses)
    3. Hard (5 misses)
    """)
    return int(input("Select Level:"))  #Asks user which level they want to play

def wantsToPlay():
    if (not playedOnce):
        return 1
    l = input("\nWould you like to play again? (y/n)")  #Asks user if they want to play again
    while (l != "y" and l != "Y" and l != "n" and l != "N"):
        l = input("\nWould you like to play again? (y/n)")
    if (l.lower() == "y"):
        return 1
    return 0

def takeNewLetter():
    global state, hasWon
    newPrint("So far, you have guessed the following letters...")
    for g in guessed:
        print(g, end=" ")
    letter = input("\n\nChoose another letter:\n")
    while (letter in guessed or letter not in ACCEPTABLE):  #if the chosen letter is in the word, user scores a point
        if (len(letter) > 1):
            if (letter.lower() == WORD.lower()):
                 newPrint("You win!")
                 hasWon = 1
                 break
            else:
                newPrint("You Lose!")
                state = 7
                break
        else:
            if (letter not in ACCEPTABLE):
                letter = input("That character is unacceptable. You many only enter lower case letters.\n")
            else:
                letter = input("You have already guessed that letter, try another one...\n")
    guessed.append(letter)
    if (letter not in WORD): #if the letter is not in the word to guess, add a line to the hangman.
        state += 1
    return

def drawWord():
    tempWord = ""
    for c in WORD:
        if (c in guessed):
            tempWord += c + " "
        else:
            tempWord += "_ "
    newPrint(tempWord)
    return
def drawStickman():
    if (state >= 7):
        print("   _______")
        print("|/      |")
        print("|      (_)")
        print("|      \|/")
        print("|       |")
        print("|      / \\")
        print("|")
        print("|___")
        print("Oops. You're dead.")
    elif (state == 6):
        print("   _______")
        print("|/      |")
        print("|      (_)")
        print("|      \|/")
        print("|       |")
        print("|      / ")
        print("|")
        print("|___")
    elif (state == 5):
        print("   _______")
        print("|/      |")
        print("|      (_)")
        print("|      \|/")
        print("|       |")
        print("|")
        print("|")
        print("|___")
    elif (state == 4):
        print("   _______")
        print("|/      |")
        print("|      (_)")
        print("|      \|/")
        print("|")
        print("|")
        print("|")
        print("|___")
    elif (state == 3):
        print("   _______")
        print("|/      |")
        print("|      (_)")
        print("|      \|")
        print("|")
        print("|")
        print("|")
        print("|___")
    elif (state == 2):
        print("   _______")
        print("|/      |")
        print("|      (_)")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|___")
    elif (state == 2):
        print("   _______")
        print("|/      |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|___")
    elif (state == 1):
        newPrint("As this is your first mistake, I will let you off...")
        print("   _______")
        print("|/")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|___")
    elif (state == 0):
        print("   _______")
        print("|/")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|___")

def hasGuessed():
    if (hasWon == 1):
        return 1
    if (state >= 7):
        return 1
    for c in WORD:
        if (c not in guessed):
            return 0
    if (len(guessed) == 0):
        return 0
    return 1

def setup_game():
    newPrint("Welcome to the Hangman game!")
    newPrint("I have chosen a random word from my super secret list, try to guess it before your stickman dies!")

def newPrint(message, both = 1):
    msg = "\n" + message
    if (both != 1):
        msg += "\n"
    print(msg)

def scoring():
    score = 0
    if WORD == WORD.lower():
        score = score + 1   #add one point to user's score
    print("Your current score is", score)
    with open("scores.txt") as source:  #main file to store user's scores
        userNames = [line.strip().split(', ')[1] for line in source]  # Populates a list with the usernames in the file
    with open("scores.txt") as source:
        scores = [line.strip().split(', ')[2] for line in source]  # Populates a list with their scores in the file

def main():
    global guessed, hasWon, state, playedOnce, WORD, WORDLIST   #these variables have to be global as they're used throughout the whole program
    setup_game()
    newPrint("The word is " + str(len(WORD)) + " letters long.")
    while (wantsToPlay() == 1):
        WORD = random.choice(WORDLIST)
        guessed = []    #stores the guessed words in this list
        playedOnce = 1
        hasWon = 0
        state = 0
        while (hasGuessed() == 0 and state < 7):
            drawStickman()
            drawWord()
            takeNewLetter()
        drawStickman()
        newPrint("The word was " + WORD)

main()
