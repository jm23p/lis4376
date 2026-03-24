def get_requirements():
    """function prints program requirements"""
    print("Simple Shopping Cart!")
    print("\nProgram Requirements:\n"
          + "Developer: Joshua Mann\n"
          + "1. Capture user-entered shopping items.\n"
          + "2. Retrieve cost for each item.\n"
          + "3. Print items, cost, and total of all items.\n"
          + "4. Must perform data and range validation.\n")
    
    print("Input:")

# Input/Process/Output: IPO

def add_items():
    """accepts 0 args. prompts for item names, returns user-entered values, including item count"""
    # test string input

    print("Enter -1 to stop program.\n")

    # initialize variables
    name = ""
    count = 0
    my_items = []

    # note: -1 flag value
    while name != "-1":
        try:
            # prompt for item name
            print("{0}{1}{2}".format(
                "Enter item", count + 1, " name: "), end="")
            
            name = input()
            name[0] # test for input

            # stop loop with flag value
            if name == "-1":
                print("Stopping list!\n")
                break

            count += 1 # increment counter variable
            my_items.append(name) # if all OK, append cart item

        except IndexError as e:
            # print(e) # only used to print generated error message
            print("No item name entered! Try again.\n")
            continue

    return my_items

def get_items_cost(items_list):
    """accepts o args. prompts for item amount, returns user-entered value"""
    # test valid float and w/in range

    # initialize variables
    i = 0 # list item counter variable
    my_cost = [] # shopping cart list items cost

    for my_iterator in range(len(items_list)):
        while True:
            try:
                # initialize variable(s)
                cost = 0.0

                # prompt for item cost
                print("{0}{1}{2}".format("Enter ", items_list[i], " cost: $"), end="")

                cost = float(input())

                is_within_range = False
                while not is_within_range:
                    if cost >= 1 and cost <= 100:
                        is_within_range = True
                    else:
                        print("Item cost must be between $1 and $100.\n")
                        print("{0}{1}{2}".format(
                            "Enter", items_list[i], "cost: $"), end="")
                        cost = float(input())

                i += 1
                my_cost.append(cost)
                break

            except ValueError:
                print("Not a float! Try again.\n")
                continue

    return my_cost

def get_cart(items, costs):
    # initialize variables
    j = 0 # initialize counter variable
    total = 0.0 # cart total

    print() # give vertical space

    # display table header
    print("{0:<10s}{1:<12s}".format("Item", "Cost"))

    while j < len(items):
        print("{0:<12s}{1:>6.2f}".format(items[j], costs[j]))
        total = total + costs[j] # accumulate total
        j += 1 # increment counter variable

    # display total
    print("\nTotal: ${0:,.2f}".format(total))