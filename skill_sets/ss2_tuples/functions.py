def get_requirements():
    """function prints program requirements"""
    print("Python Lists")
    print("\nProgram Requirements:\n"
          + "Developer: Joshua Mann\n"
          + "1. Tuples (Python data structure): *immutable* (cannot be changed), ordered sequence of elements.\n"
          + "2. Tuples are immutable/unchangeable - that is, cannot insert, update, delete.\n"
          + "3. Create tuple using parentheses (tuple): tuple = (include below list elements here...)\n"
          + "4. Reassign tuple with, and w/o parentheses (), aka tuple \"packing.\n"
          + "5. Use tuple (unpacking), that is, assign values from tuple to sequence of variables: elem1, elem2, elem3, elem4 = my_tuple\n"
          + "6. Backward-engineer the following program.\n")
    
def get_tuple():
    """function to create my_tuple"""
    # initialize my_tuple
    my_tuple = (1, "test", 3.14, True)
    print("Print my_tuple: ", end="")
    print(my_tuple)

    return my_tuple

def unpack_tuple(num_tuple):
    """function to unpack my_tuple"""
    # my_tuple unpacking
    elem1, elem2, elem3, elem4 = num_tuple
    print("\nPrint my_tuple unpacking:")
    print("elem1=", elem1, ", elem2=", elem2, 
        ", elem3=", elem3, ", elem4=", elem4, sep="")
    
def count_tuple(num_tuple):
    """function to count my_tuple elements"""
    print("\nDisplay number of my_tuple elements: ")
    # also works for strings, tuples, dict objects
    print(len(num_tuple))

def parse_tuple(num_tuple):
    """function to parse my_tuple elements"""
    print("\nPrint third element in my_tuple:")
    print(num_tuple[2])

    print("\nPrint \"slice\" of my_tuple (second and third elements):")
    print(num_tuple[1:3])

def reassign_tuple(num_tuple):
    print("\nReassign my_tuple using parentheses.")
    num_tuple = (1, 2, 3, 4)
    print("Print reassigned my_tuple:")
    print(num_tuple)

    print("\nReassign my_tuple using \"packing\" method (no parentheses).")
    num_tuple = 5, 6, 7, 8

    print("Print reassigned my_tuple:")
    print(num_tuple)

def remove_tuple(num_tuple):
    print("\nDelete my_tuple: \nNote: will generate error, if trying to print after delete, as it no longer exists.")
    del num_tuple
    # print(num_tuple) # note: will generate error, as it no longer exists