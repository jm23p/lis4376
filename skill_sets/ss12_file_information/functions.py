import os
import os.path

script_dir = os.path.dirname(os.path.abspath(__file__)) # ensures the path called by list_dir() is in the repository, not the VS code path
os.chdir(script_dir)

"""Defines nine functions:

1. get_requirements()
2. get_menu()
3. run_command()
4. list_dir()
5. move_up()
6. move_down()
7. num_files()
8. num_bytes()
9. find_files()
"""

# create constants
COMMANDS = ('1', '2', '3', '4', '5', '6', '7')
MENU = """1 List
2 Up
3 Down
4 Count
5 Size
6 Search
7 Quit"""

def get_requirements():
    """function prints program requirements"""
    print("Program provides file system navigation and information.")
    print("\nProgram Requirements:\n"
          + "Developer: Joshua Mann\n"
          + "1. Write program functions that navigate and display file system information.\n"
          + "2. Create and display program menu.\n"
          + "3. Must prevent incorrect command input.\n")
    
    print("Input:")

def get_menu():
    """accepts 0 args. prints current working directory, and displays menu items."""
    print("\nCurrent working directory:\n", os.getcwd(), "\n")
    print("MENU:\n", MENU, sep="")

def get_command():
    """accepts 0 args. returns command number, or error message."""
    while True:
        command = input("\nEnter command: ")
        if not command in COMMANDS:
            print("Incorrect command!")
        else:
            return command
        
def run_command(command):
    """accepts 1 arg. runs command based upon user-entered value."""
    if command == '1':
        list_dir(os.getcwd()) # lists cwd files and folders
    elif command == '2':
        move_up() # move to parent directory
    elif command == '3':
        move_down(os.getcwd()) # move to named subdirectory
    elif command == '4':
        print("total files:",
              num_files(os.getcwd())) # cwd file count
    elif command == '5':
        size = num_bytes(os.getcwd())
        print("{0}{1: ,d}{2}{3: ,.2f}{4}{5: ,.2f}{6}{7: ,.4f}{8}".format("\nTotal size:\n", size, "bytes\n", size / 1000, "KB\n", size / 1000000, "MB\n", size / 1000000000, "GB"))
    elif command == '6':
        my_file = input("Enter file name: ")
        file_list = find_files(my_file, os.getcwd())
        if not file_list:
            print("File not found")
        else:
            # list found file in cwd and subdirectories
            print("\n File paths for ", my_file, ":", sep="")
            for f in file_list:
                print(f)

def list_dir(dir_name):
    """accepts 1 arg. list all files and directories in current working directory."""
    print("\nAll files and directories in ","", dir_name, ":", sep="") # ensure this matches proper code
    my_list = os.listdir(dir_name)
    for element in my_list:
        print(element)

def move_up():
    """accepts 0 args. move up to parent directory"""
    os.chdir("..")

def move_down(cur_dir):
    """accepts 1 arg. move down to named subdirectory - if it exists"""
    my_dir = input("Enter directory name: ")
    if os.path.exists(cur_dir + os.sep + my_dir) and \
        os.path.isdir(my_dir):
            os.chdir(my_dir)
    else:
        print("Incorrect directory name!")

def num_files(path):
    """accepts 1 arg. returns file count of current working directory and subdirectories"""
    count = 0
    my_list = os.listdir(path)
    for element in my_list:
        if os.path.isfile(element):
            count += 1
        else:
            os.chdir(element)
            count += num_files(os.getcwd())
            os.chdir("..")
    return count

def num_bytes(path):
    """accepts 1 arg. returns number of bytes in current working directory and subdirectories"""
    size = 0
    my_list = os.listdir(path)
    for element in my_list:
        if os.path.isfile(element):
            size += os.path.getsize(element)
        else:
            os.chdir(element)
            size += num_bytes(os.getcwd())
            os.chdir("..")
    return size

def find_files(my_file, path):
    """accepts 2 args. returns list of file names in current working directory and subdirectories"""
    files = []
    my_list = os.listdir(path)
    for element in my_list:
        if os.path.isfile(element):
            if my_file in element:
                files.append(path + os.sep + element)
        else:
            os.chdir(element)
            files.extend(find_files(my_file, os.getcwd()))
            os.chdir("..")
    return files