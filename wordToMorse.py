import string

# Main program
def main():
    userInput = input("Word: ").lower()
    letterToMorse = dictionary()
    newString = ""

    # Check for every letter in line 5
    for i in userInput:
      
# Checks if that letter is in dictionary if True it returns the value of that letter
        if i in letterToMorse:
            newString += str(letterToMorse[i]) + " "
          
# Removes the last slice of string which in this case will always be " "
    newString = newString[:-1]
    return newString





def dictionary():
    # imports the letters in the alphabet from A-Z in lowercase
    alphabet = string.ascii_lowercase

    
    morseCode = ['•-', '-•••', '-•-•', '-••', '•', '••-•', '--•', '••••', '••', '•---', '-•-', '•-••',\
    '--', '-•', '---', '•--•', '--•-', '•-•', '•••', '-', '••-', '•••-', '•--', '-••-', '-•--', '--••']

    mydict = {}

    # For every letter in the alphabet, assign the letter with the value in morse code
    # Note that the list "morseCode" is in alphabetical order aswell.
    for i in range(len(alphabet)):
        mydict[alphabet[i]] = morseCode[i]
    
    return mydict

print(main())
