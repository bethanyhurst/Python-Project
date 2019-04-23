import string

def caesar():
    number = random.randint(0, 25) #Choose a shift
    shift = random.randint(0, 25) #Choose a shift
    generateQuestion = random.randint(0, 1) #Choose encode or decode
    alphabetList = list(string.ascii_uppercase) #Put the alphabet into a list
    alphabet = list(string.ascii_uppercase) #Put the alphabet into a list
    if generateQuestion == 0: #Encode
        queston1 = "encrypt this message using shift 3: LETSPLAYHANGMAN"
        codedMessage = []
        for char in message:
            if char in alphabet:
                charPos = alphabet.index(char)
            newCharPos =( charPos + shift) % LEN
            codedMessage.append(alphabet[newCharPos])
    numOfAttempts = 3
    while numOfAttempts> 0:
        print("type your answer, you have " + str(numOfAttempts) + "attempts left")

        if response == "OHWVSODBKDQJPDQ":
            print("Well done!")

        else:
            print("Incorrect! Try again.")
            numOfAttempts -= 1

    else: #Decode
        question2 = "Decrypt this message using Caeser Cipher: CROPPSOVNRKVVKW"
        shift = shift * -1
    numOfAttempts = 3
    while numOfAttempts> 0:
        print("type your answer, you have " + str(numOfAttempts) + "attempts left")

        if response == "SHEFFIELDHALLAM":
            print("Well done!")

        else:
            print("Incorrect! Try again.")
            numOfAttempts -= 1

def vigenere():
    table = []
    number = random.randint(0, 25)
    generateQuestion = (1, 2)
    if generateQuestion == 1: #Encode question
        question3 = "Encrypt this message using the Vigenere Cipher: CAMOUFLAGE, key word: HIDDEN"
        for i in range(25):
            table.append([])

    for row in range(25):
        for column in range(25):
            if (row + 65) + column > 90:
                # moving back to A after Z
                # after first row, each letter will shift left by one position compared to row above it
                table[row].append(chr((row+65) + column - 26))
            else:
                # after first row, each letter will shift left by one position compared to row above it
                table[row].append(chr((row+65)+column))
    numOfAttempts = 3
    while numOfAttempts> 0:
        print("type your answer, you have " + str(numOfAttempts) + "attempts left")

        if response == "JIPRYSSIJH ":
            print("Well done!")

        else:
            print("Incorrect! Try again.")
            numOfAttempts -= 1

    else:
        question4 = "Decrypt this message using the Vigenere Cipher: NIPIGNPWKEW key word: GAME"

    numOfAttempts = 3
    while numOfAttempts> 0:
        print("type your answer, you have " + str(numOfAttempts) + "attempts left")

        if response == "HIDEANDSEEK":
            print("Well done!")

        else:
            print("Incorrect! Try again.")
            numOfAttempts -= 1

    return table


def cipher_encryption(message, mapped_key):
    table = create_vigenere_table()
    encrypted_text = ""

    for i in range(len(message)):
        if message[i] == chr(32):
            # ignoring space
            encrypted_text += " "
        else:
            # getting element at specific index of table
            row = ord(message[i])-65
            column = ord(mapped_key[i]) - 65
            encrypted_text += table[row][column]

    print("Encrypted Message: {}".format(encrypted_text))


def itr_count(mapped_key, message):
    counter = 0
    result = ""

    # starting alphabets from mapped_key letter and finishing all 26 letters from it, (after z we move to a)
    for i in range(26):
        if mapped_key + i > 90:
            result += chr(mapped_key+(i-26))
        else:
            result += chr(mapped_key+i)

    # counting the number of iterations it take from mapped key letter to ciphertext letter
    for i in range(len(result)):
        if result[i] == chr(message):
            break
        else:
            counter += 1

    return counter


def cipher_decryption(message, mapped_key):
    table = create_vigenere_table()
    decrypted_text = ""

    for i in range(len(message)):
        if message[i] == chr(32):
            # ignoring space
            decrypted_text += " "
        else:
            # adding number of iterations, it takes to reach from mapped key letter to cipher letter in 65
            # by doing so we get column header of ciphertext letter, which happens to be decrypted letter
            decrypted_text += chr(65 + itr_count(ord(mapped_key[i]), ord(message[i])))

    print("Decrypted Message: {}".format(decrypted_text))

if __name__ == "__main__":
    main()
