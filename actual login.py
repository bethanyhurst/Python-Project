# A program that generates a unique username for a given name
# along with a password then stores this information in a file
# with the password being stored as a hashed value

import random
import hashlib

def main():
      status = input("Do you already have an account? yes/no? Press q to quit")
      if status == "yes":
        returningUser()
      elif status == "no":
        newUser()

def returningUser():

    ## not complete yet
        count = 0
        try: # If the users.txt file exists, open it
         with open("users.txt") as source:
           userNames = [line.strip().split(', ')[1] for line in source]# Populates a list with the usernames in the file
         with open("users.txt") as source:
            passwords = [line.strip().split(', ')[2] for line in source]# Populates a list with the passwords in the file
        except: # If not
         userNames = [] # Set an empty list for the usernames
         passwords = [] # Set an empty list for the passwords


         returnUserName = input("Enter username")
         returnPassword = input("Enter password")
         returnPassword = hashlib.md5(returnPassword.encode())


         for items in userNames:
            if returnUserName == userNames and returnPassword == passwords:
             print("You are now logged in")
             return
         else:
                print("incorrect credentials")
                count += 1


def newUser():
    try: # If the users.txt file exists, open it
        with open("users.txt") as source:
           userNames = [line.strip().split(', ')[1] for line in source]# Populates a list with the usernames in the file
        with open("users.txt") as source:
            passwords = [line.strip().split(', ')[2] for line in source]# Populates a list with the passwords in the file
    except: # If not
        userNames = [] # Set an empty list for the usernames
        passwords = [] # Set an empty list for the passwords

    newUser = input("What is the user's name?\n") # Get the name of the user
    initials = ("".join(name[0] for name in newUser.split())) # Get the initials of the user
    randDigits = random.randint(1000, 9999) # Get a random number
    uName = initials + str(randDigits) # Put the random number on the end of the initials

    while uName in userNames: # While the username already exists
       ranDigits = random.randint(1000, 9999) #Generate a new random number
       uName = initials + str(randDigits) # Add the new number to the end of the initials
    print ("username is", uName)

    with open("sowpods.txt") as source: #Open the files of passwords
       validChoices = [line.strip() for line in source if len(line) in range(9, 12)]
    # Get the passwords between 9 and 12 characters long into a list

    password = random.choice(validChoices) # Choose a random password from those passwords

    while password in passwords: #  While the password chosen has already been used
        password = random.choice(validChoices) # Choose a new password
    print("Their password is ", password) # Display the user's password

    with open("users.txt", "a") as destination: # Open the file with the users' data
       hVal = hashlib.md5(password.encode()) # Encode the password
       destination.write(uName + "," + hVal.hexdigest() + "\n")# Dump the user's data in the fileS

main()


