import random
import os


# Workaround for Python2
try:
    input = raw_input
except NameError:
    pass

# Let's set the colours
# Define different colour commands
win_colour_dict = {
    'cmd'   : 'color ',
    'colours': {
        'pass'  : 'A0',
        'fail'  : '4F',
        'start' : '30',
        'last'  : '60',
        'reset' : '0F'
    }
}

ansi_colour_dict = {
    'cmd'   : 'echo -e ',
    'colours': {
        'pass'  : r'"\e[38;2;0;255;0m"',
        'fail'  : r'"\e[38;2;255;0;0m"',
        'start' : r'"\e[38;2;0;255;255m"',
        'last'  : r'"\e[38;2;255;255;0m"',
        'reset' : r'"\e[38m"'
    }
}

# Choose the colour command set based on OS
if os.name == 'nt':
    temp_dict   = win_colour_dict
else:
    temp_dict   = ansi_colour_dict

# Generate the command table
colour_dict = {}
for colour, command in temp_dict['colours'].items():
    colour_dict[colour] = temp_dict['cmd'] + command

# Some settings for the game
TOTAL_TURNS     = 8
TOTAL_COLOURS   = 6
TOTAL_CODE      = 4

# Location fo the code to crack
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

def print_exit_message():
    input("Press enter to exit...")
    set_colour('reset')
    exit()

# Helper functions
def big_divider():
    return "=========================================="
def small_divider():
    return "------------------------------------------"

def set_colour(colour):
    os.system(colour_dict[colour])

# Print greetings
set_colour('start')

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
        set_colour('last')
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
        set_colour('pass')
        print(big_divider())
        print("Code:")
        print(CODE)
        print("WON!!!")
        print_exit_message()

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
set_colour('fail')
print(big_divider())
print("Code:")
print(CODE)
print("LOST!!!")
print_exit_message()