##http://easygui.sourceforge.net/tutorial.html - For using easyGUI
##https://cvstuff.wordpress.com/2014/11/27/wraping-c-code-with-python-ctypes-memory-and-pointers/ - For using Ctypes

from easygui import *
import sys

def showHub(): #Hub screen to choose a feature of the program
    functions = [showHangman,showQuiz,showLogon] #List of the functions to leaunch the different areas of the program
    choices=["Hangman", "Quiz", "Log out"] #List of the options given to the user
    selected = indexbox("What do you want to do?", choices=choices) #Display the options to the user and get their chosen one
    functions[selected]() #Run the chosen function

def showHangman(): #Launch hangman
    print("Hangman")

def showQuiz(): #Launch the quiz
    print("Quiz")

def showAccountCreate(): #Allow the user to create an account
    createHeader = "Create your account" #Title of the page
    createMsg = "Enter your chosen username and password" #Main message
    createFields = ["Username","Password"] #Entry fields
    createEntries = [] #Results given by the user
    errMsg = ""

    while 1: #Keep asking for entries until entered data is valid
        createEntries = multpasswordbox(createMsg + errMsg, createHeader, createFields) #Display fields and get entries back
        if(createEntries is None): #If cancel is clicked
            sys.exit(0) #Close the program
        elif(createEntries[1] == ""): #Check validity of entered data
            errMsg = ". Need to enter a password."
        else: #If all data is valid
            break

    errMsg = ""
    while 1: #Keep the password re-entry form up
        password = passwordbox("Re-enter your password. " + errMsg, " ",)
        #Ask for the password, showing an error message is applicable

        if(password == createEntries[1]): #If re-entry is the same
            #Write account info to file hashed
            print("Write to file")
            showLogon()
            break
        elif(password is None): #If cancel was clicked
            showAccountCreate() #Re-start account creation
        else: #If the passwords do not match
            errMsg = ("Entered password is not the same!") #Create error message

def logonCheck(loginEntries):
    returnVal = False
    if(loginEntries[1] == "1"):
        returnVal = True
    return(returnVal)

def showLogon(): #Launch the login screen
    attempts = 3
    detailsCorrect = False
    try:
        reading = open("users.txt") #Try to open the accounts file
        dataExists = True #The file exists - the program has been run before
    except:
        dataExists = False #The file doesn't exist - this is the first run of the program

    dataExists = True ###Uncomment to ignore first run check ------------------

    if (dataExists == True): #If this isn't the first run
        loginHeader = "Login"
        loginMsg = "Enter your login information"
        loginFields = ["Username","Password"]
        while 1:
            loginEntries = []
            loginEntries = multpasswordbox(loginMsg,loginHeader,loginFields)
            if(loginEntries is None): #If cancel is clicked
                sys.exit(0) #Close the program
            else:
                #Check username + password against stored values
                detailsCorrect = logonCheck(loginEntries)
                if(detailsCorrect == True):
                    showHub()
                else:
                    attempts -= 1
                    if(attempts > 0):
                        loginMsg = "Incorrect details - " + str(attempts) + " attempts left."
                    else:
                        msgbox("You have run out of login attempts.")
                        break
            #showHub() #Uncomment to skip login entry
    else: #If this is the first run
        showAccountCreate() #Get the user to create an account

showLogon() #Start