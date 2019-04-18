messageToEncode = "help! get me out of here"

fenceHeight = 4

encodedMessage = ""
for k in range(fenceHeight):
    encodedMessage += messageToEncode[k: : fenceHeight]

print('"' + messageToEncode + '" BECOMES: "' + encodedMessage + '"')
