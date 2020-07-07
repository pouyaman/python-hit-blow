import random
import os


# Workaround for Python2
try:
    input = raw_input
except NameError:
    pass

# Let's set the colour
os.system('color 70') # B: Gray, T:Black


TOTAL_TURNS     = 8
TOTAL_COLOURS   = 6
TOTAL_CODE      = 4

CODE            = []

# Valid numbers
VALID_RANGE = range(1,TOTAL_COLOURS+1)

# Generate random Code to be broken
while(1):
    digit = random.randint(1, TOTAL_COLOURS)
    if digit not in CODE:
        CODE.append(digit)
    if len(CODE) == TOTAL_CODE:
        break

# Retrieve input from user and basic checks
def get_input():
    result = None
    number = input("Give number:\n")

    if len(number) != TOTAL_CODE:
        print("Code should be %i digits" %TOTAL_CODE)
        return None

    for c in number:
        digit = int(c)
        if digit not in VALID_RANGE:
            print("%s not valid..." %c)
            print("Each digit of code should a number between 1 and %i" %TOTAL_COLOURS)
            return None
        if result is None:
            result = []
        result.append(digit)

    return result

# Helper functions
def big_divider():
    return "=========================================="
def small_divider():
    return "------------------------------------------"

# Print greetings
print("Welcome to Hit & Blow!")
print(big_divider())
print("Guess a %i digit number."            %TOTAL_CODE)
print("Each digit ranging from [1 to %i]."  %TOTAL_COLOURS)
print("You have %i turns."                  %TOTAL_TURNS)
print("")
print("Hits : Correct colour and spot")
print("Blows: Correct colour only")

# Start Loop
turn = 0
while(turn < TOTAL_TURNS):
    turn+=1

    # Setup
    hits    = [None] # make index 0 = None, so the list index matches the digit starting from 1
    blows   = [None]
    for i in VALID_RANGE:
        hits.append( None)
        blows.append(None)

    # Print info
    print(small_divider())
    if(turn == TOTAL_TURNS):
        print("!!!LAST TURN!!!")
    else:
        print("Turn: %i" %turn)

    # Retrieve input from user
    numbers = get_input()

    # Check the input
    if numbers is None:
        print("Turn not lost.")
        print("Try again!")
        turn-=1
        continue

    # Did they win??
    if numbers == CODE:
        print(big_divider())
        print("Code:")
        print(CODE)
        print("WON!!!")
        os.system('color A0') # B: Green, T: Black
        input("Press enter to exit...")
        exit()

    # Check each digit
    for i, digit in enumerate(numbers):
        if digit == CODE[i]: # find hit and cancel prior blow/prevent future blow for that number
            hits[ digit]    = 1
            blows[digit]    = 0
        elif blows[digit] != 0 and digit in CODE: # mark blow if that number hasn't had a hit yet
            blows[digit]    = 1

    # Let user know what the total hit and blows are
    print("Hits : %i" %hits.count(1))
    print("Blows: %i" %blows.count(1) )

# Let user know they failed :(
print(big_divider())
print(CODE)
print("LOST!!!")
os.system('color 4F') # B: Red, T: White
input("Press enter to exit...")
