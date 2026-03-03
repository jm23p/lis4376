"""main file to run functions library"""
import functions as f

def main():
    """function to pull from function library"""
    # initialize variables
    low_num = 0
    high_num = 0
    
    # function calls
    f.get_requirements()
    low_num = f.get_lower()
    high_num = f.get_upper()

    while low_num > high_num:
        print("Lower number must be less than or equal to upper number! Try again!\n")
        low_num = f.get_lower()

    f.play_game(low_num, high_num)

if __name__ =="__main__":
    main()