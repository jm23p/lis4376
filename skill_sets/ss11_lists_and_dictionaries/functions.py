def get_requirements():
    """function prints program requirements"""
    print("")
    print("\nProgram Requirements:\n"
          + "Developer: Joshua Mann\n"
          + "1. Write a program that prints all elements of a user-entered contact list.\n"
          + "2. Must perform data validation.\n"
          + "3. Dictionary key *must* be user's e-mail address.\n")
    
def add_emails():
    """accepts 0 args. prompts for emails, returns user-entered values, including email count. with data validation"""
    # test string input (cant simply be string)

    print("Enter -1 to stop adding e-mails.\n")

    # initialize variable(s)
    email = ""
    count = 0
    my_emails = []

    # note: -1 flag value
    while email != "-1":
        try:
            # prompt for email (note: no newline, and counter variable to make user-friendly)
            print("{0} {1}{2}".format(
                "Enter email", count + 1, ": "), end="")
            
            email = input()
            # test for input (access first character, if none, error)
            email[0]

            # stop loop with flag value
            if email == "-1":
                print("Stopping list!")
                break

            count+= 1 # increment counter variable
            my_emails.append(email) # if all ok, append cart email

        except IndexError as e:
            # print(e) # only used for testing, to print generated error message
            print("No email entered! Try again.\n")
            continue

    return my_emails

def get_phones(emails_list):
    """accepts 1 arg. prompts for phone numbers, based upon emails, returns user-entered values. with data validation"""
    # test string input (cant simply be string)

    # initialize variables
    phone = ""
    i = 0 # list email counter variable
    my_phones = [] # phone list

    for my_iterator in range(len(emails_list)):
        while True:
            try:
                print("\n{0}{1}".format(emails_list[i], ", phone:"))

                phone = input()

                # test for input (access first character, if none, error)
                phone[0]

                i += 1 # increment list item variable
                my_phones.append(phone) # if all ok, append cart phone
                break

            except IndexError as e:
                print("No phone entered! Try again.")
                continue

    return my_phones

def create_contact(keys, values):
    """accepts 2 args. creates dictionary based upon two list parameters. displays dictionary elements"""
    my_dictionary = {} 

    # note: zip() function conjoins elements in two lists; dict() converts resulting tuples into dictionary key-value pairs
    my_dictionary = dict(zip(keys, values))

    # testing returns
    # print(type(my_dictionary))
    # exit()

    """
    Following three functions returned through dictionary object:
    .keys() returns keys
    .values() returns values
    .items() returns both keys and values
    """

    print("\nPrinting ddictionary:\n", my_dictionary)
    print("\nPrinting ddictionary keys:\n", my_dictionary.keys())
    print("\nPrinting ddictionary values:\n", my_dictionary.values())
    print("\nPrinting ddictionary items:\n", my_dictionary.items())