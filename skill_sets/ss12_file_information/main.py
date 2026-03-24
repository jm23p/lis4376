"""main file to run functions library"""
import functions as f

def main():
    """function to pull from function library"""
    f.get_requirements()

    while True:
        f.get_menu() # display cwd and menu before each command
        command = f.get_command()

        if command != "7":
            f.run_command(command)
        else:
            print("\nStopping program!")
            break

if __name__ =="__main__":
    main()