"""defines four functions"""
import random

def get_requirements():
    """function prints program requirements"""
    print("Guessing Game!")
    print("\nProgram Requirements:\n"
          + "Developer: Joshua Mann\n"
          + "1. Create guessing game based upon pseudo-random numbers.\n"
          + "2. Must perform data and range validation.\n")
    
    print("Input:")

def get_lower():
    """accepts 0 args. prompts for lower number, returns user-entered value."""
    # test valid int and w/in range
    while True:
        try:
            # initialize variable(s)
            lower = 0

            # prompt lower number
            lower = int(input("Enter lower number: "))

            is_within_range = False
            while not is_within_range:
                if lower >= -1000 and lower <= 1000:
                    is_within_range = True
                else:
                    print("Lower must be between -1000 and 1000.\n")
                    lower = int(input("Enter lower: "))

        except ValueError:
            print("Not an int! Try again.\n")
            continue
        else:
            return lower
        
def get_upper():
    """accepts 0 args. prompts for upper number, returns user-entered value"""
    # test valid int and w/in range
    while True:
        try:
            # initilize variable(s)
            upper = 0

            # prompt upper number
            upper = int(input("Enter upper number: "))

            is_within_range = False
            while not is_within_range:
                if upper >= -1000 and upper <= 1000:
                    is_within_range = True
                else:
                    print("Upper must be between -1000 and 1000.\n")
                    upper = int(input("Enter upper: "))

        except ValueError:
            print("Not an int! Try again.\n")
            continue
        else:
            return upper
        
def play_game(lower, upper):
    """accepts 2 args. creates pseudo-random number based upon user-entered values, and prompts users to guess."""
    # initialize variables
    count = 0

    # generate random int between lower and upper number (inclusive of both start and end values)
    rand_int = random.randint(lower, upper)

    while True:
        count += 1
        guess = int(input("\nEnter guess: "))

        if guess < rand_int:
            print("Too low!")
        elif guess > rand_int:
            print("Too high!")
        else:
            print("Bingo! Number of tries:", count)
            break