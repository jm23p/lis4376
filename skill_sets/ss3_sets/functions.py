def get_requirements():
    """function prints program requirements"""
    print("Python Sets - like mathematical sets!")
    print("\nProgram Requirements:\n"
          + "Developer: Joshua Mann\n"
          + "1. Sets (Python data structure): mutable, heterogeneous, undordered sequence of elements, CANNOT contain duplicate values.\n"
          + "2. Sets are mutable/changeable - that is, can insert, update, delete.\n"
          + "3. While sets are mutable/changeable, they *cannot* contain other mutable items like list, set, or dictionary--\n"
          + "4. Also, since sets are unordered, CANNOT use indexing (or, slicing) to access, update, or delete elements.\n"
          + "5. Two methods to create sets:\n"
          + "\ta. Create set using curly brackets {set}: set1 = {include below set elements here...}\n"
          + "\tb. Create set using set() function: set1 = set( <iterable> )\n\n"
          + "\tExamples:\n"
          + "\tset2 = set([include below set elements here...]) # set with list\n"
          + "\tset3 = set((include below set elements here...)) # set with tuple\n"
          + "\tNote: An \"iterable\" is *any* object, which can be iterated over--that is, lists, tuples, or even strings.\n"
          + "6. Backward-engineer the following program.\n")
    
def get_set():
    """function to create set1"""
    print("***Note***: All three sets below print as \"sets\" (i.e., curly brackets), *regardless* of how they were created!\n")

    """
    Note:
    True=1, False=0
    Sets do not allow duplicate elements.
    Therefore, if sets are unordered, {1,2} and {2,1} are the same set!
    """

    # initialize set1
    set1 = {2, "test", 3.14, True} # create set
    print("Print set1 created using curly brackets:\n"
          + "Note: following values used: 2, \"test\", 3.14, True\n"
          + "Note: Value sequence *used* not guaranteed!")
    print(set1)
    # note: each run displays strings in different order, number always sequential

    print("\nPrint set1 type:")
    print(type(set1))

    return set1

def get_other_sets():
    """function to create other sets"""
    set2 = set([2, "test", 3.14, True])
    print("\nPrint set2 created using set() function with list:")
    print(set2)

    print("\nPrint set2 type:")
    print(type(set2))

    set3 = set((2, "test", 3.14, True))
    print("\nPrint set3 created using set() function with tuple:")
    print(set3)

    print("\nPrint set3 type:")
    print(type(set3))

    """
    Note:
    A set can be empty. However, Python interprets empty curly braces as an empty dictionary!
    So, only way to define an *empty* set is with set() function:
    x = set()
    type(x)
    <class 'set'>
    """

def count_set(num_set):
    """function to count set elements"""
    print("\nDisplay number of set1 elements: ")
    print(len(num_set))

def add_set(num_set):
    """function to add set elements"""
    print("\nAdd set element (5) using add() method:")
    num_set.add(5)
    print(num_set)

    print("\nDisplay number of set1 elements:")
    print(len(num_set))

def update_set(num_set):
    """function to update set elements"""
    num_set.update({1, 2, 3, 4})

    print("\nDisplay updated set1 elements:\n"
          + "Note: Updated with following values: 1, 2, 3, 4\n"
          + "Note: Sets can ONLY contain unique elements! (Note: True=1, and value 2 already exist!)")
    print(num_set)

    print("\nDisplay number of set1 elements: ")
    print(len(num_set))

def discard_element(num_set):
    """function to discard set element"""
    print("\nDiscard 4:")
    num_set.discard(4)
    print(num_set)

    print("\nLength of set1:")
    print(len(num_set))

def remove_element(num_set):
    """function to remove set element"""
    print("\nRemove 'test':")
    num_set.remove('test')
    print(num_set)

    print("\nLength of set1:")
    print(len(num_set))

    print("\nNote: When deleting set element that doesn't exist, discard() ignores it, but remove() raises KeyError!")

def min_element(num_set):
    """function to get min set element"""
    print("\nDisplay minimum value (Note: True=1):")
    print(min(num_set))

def max_element(num_set):
    """function to get max set element"""
    print("\nDisplay maximum value:")
    print(max(num_set))

def sum_elements(num_set):
    """function to sum set elements"""
    # num_set = {1, 2, 3, 4, 5} # overwrite set
    print("\nDisplay set1 elements: ")
    print(num_set)

    print("\nDisplay sum of values (*must* be numeric, or able to convert to numeric):")
    print(sum(num_set))

def clear_set(num_set):
    """function to clear/delete ALL set elements"""
    print("\nDelete all set elements:")
    num_set.clear()
    print(num_set)

    print("\nLength of set1:")
    print(len(num_set))