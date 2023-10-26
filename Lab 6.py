

# Cop3502c - Lab 6 - Encoder Decoder GitHub

# Program Functions
def encoder(num):       # Jeffery Gao
    encodedNum = ""          # encodes input
    for x in num:
        number = int(x)+3
        if number >= 10:
            number -= 10
        encodedNum += str(number)
    return encodedNum

def decoder(num):   # Matthew Cardenas
    passw = ''          # decodes input
    for number in num:
        val = int(number)
        if val <= 2:
            val += 7
        else:
            val -= 3
        passw += str(val)
    return passw

# Loops the program until quit
while True:
    # Initiates menu
    print("\nMenu")
    for char in "Menu":
        print("---",end="")
    print("\n1. Encode", "2. Decode", "3. Quit", sep="\n")

    optionChosen = int(input("\nPlease enter an option: "))       # Takes menu option


    # Sets up options and their executions
    if optionChosen == 1:       # encoder: Add 3 to each char/int
        storedNum = input("Please enter your password to encode: ")
        encodedNum = encoder(storedNum)
        print(encodedNum)
        print("Your password has been encoded and stored!")


    if optionChosen == 2:       # decoder
        print(f"The encoded password is {encodedNum}, and the original password is ", end='')
        print(decoder(encodedNum), end=".\n")


    if optionChosen == 3:       # quit
        break       # breaks while loop
