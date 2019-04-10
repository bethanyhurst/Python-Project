import string
alphabet = string.ascii_lowercase
LEN = len(alphabet)

def displayMenu():
    global endValue, selected
    choices = ["encode using caesar cipher", "decode a caesar cipher", "brute force caesar cipher", "quit"]
    endValue = len(choices)
    prompt = "what would you like to do:\n"
    for k, choice in enumerate(choices):
        prompt += "\t" + str(k+1) + ") " + choice + "\n"
    selected = input(prompt)

def caesarShift():
    codedMessage = []
    for char in message:
        if char in alphabet:
            charPos = alphabet.index(char)
            newCharPos =( charPos + shift) % LEN
            codedMessage.append(alphabet[newCharPos])
        else:
            codedMessage.append(char)

    codedMessage = "".join(codedMessage)
    print("using a shift value of",shift, message, "becomes", codedMessage)


def encode():
    global message, shift
    print("encoding...")
    message = input("what message to encode?").lower()
    shift = int(input("what shift do you want to encode with?"))
    caesarShift()

def decode():
    global message, shift
    print("decoding...")
    message = input("what message to decode?").lower()
    shift = int(input("what shift was use to encode?"))
    shift *= -1
    caesarShift()

def bruteForce():
    global message, shift
    print("brute forcing")
    message = input("what message to decode?").lower()
    for shift in range(LEN):
        caesarShift()


executables = [ encode, decode, bruteForce]

selected = ""
quitKey = "q"
while selected != quitKey:
    displayMenu()
    if selected in [str(k) for k in range(1, endValue)]:
        executables[int(selected)-1]()
    elif selected == str(endValue):
        selected = quitKey
    else:
        print("input not recognised. Try again...")

#
