def get_requirements():
    """function prints program requirements"""
    print("Python Dictionaries")
    print("\nProgram Requirements:\n"
          + "Developer: Joshua Mann\n"
          + "1. Dictionaries (Python data structure): unordered key: value pairs.\n"
          + "2. Dictionary: an associative array (also known as hashes).\n"
          + "3. Any key in a dictionary is associated (or mapped) to a value (i.e., any Python data type).\n"
          + "4. Keys: must be of immutable type (string, number or tuple with immutable elements) and must be unique.\n"
          + "5. Values: can be any data type and can repeat.\n"
          + "6. Dictionaries have key-value pairs instead of single values; differentiating a dictionary from a set.\n"
          + "7. Two methods to create dictionaries:\n"
          + "\ta. Initialize dictionary with key/value pairs.\n"
          + "\tb. Create empty dictionary, using curly braces {}: my_dictionary = {}\n"
          + "\t Then, assign values to keys: my_dictionary['key1'] = \"some value\"\n"
          + "8. Backward-engineer the following program.\n")
    
def get_dictionary():
    """function to create dictionary"""
    state_capitals = {
        "Alaska": "Juneau",
        "Texas": "Austin",
        "California": "Sacramento",
        "Montana": "Helena",
        "New Mexico": "Santa Fe"
    }

    print("Print dictionary:")
    my_dictionary = state_capitals

    print(my_dictionary)
    return my_dictionary

def parse_dictionary(my_dictionary):
    """function to parse dictionary"""
    print("\nReturn dictionary's (key, value) pairs, built-in function:")
    print(my_dictionary.items())

    print("\nOr, use looping structure to return dictionary's (key, value) pairs, built-in function:")
    for k, v in my_dictionary.items():
        print("key:", k, ", value:", v, sep="")

    print("\nDisplay all keys, built-in function:")
    print(my_dictionary.keys())

    print("\nDisplay all values in dictionary, built-in function:")
    print(my_dictionary.values())

    print("\nPrint value using key:")
    print(my_dictionary['Alaska'])

def count_dictionary(my_dictionary):
    """function to count dictionary elements"""
    print("\nCount number of items (key: value pairs) in dictionary: ")
    # also works for strings, tuples, list elements
    print(len(my_dictionary))

def add_element(my_dictionary):
    """function to add dictionary element - used only for updating below"""
    my_dictionary["Arizona"] = "Scottsdale"

    print("\nPrint dictionary after added element:")
    print(my_dictionary)

def update_element(my_dictionary):
    """function to update dictionary element"""
    my_dictionary["Arizona"] = "Phoenix"

    print("\nPrint dictionary after updated element:")
    print(my_dictionary)

def delete_element(my_dictionary):
    """function to delete dictionary element"""
    print("\nDelete \"Arizona\" element:")
    del my_dictionary["Arizona"]

    print("\nPrint dictionary after deleted element:")
    print(my_dictionary)

def delete_dictionary(my_dictionary):
    print("\nDelete all dictionary elements: ")
    my_dictionary.clear() # delete all items
    print(my_dictionary)
    print(type(my_dictionary))

    del my_dictionary