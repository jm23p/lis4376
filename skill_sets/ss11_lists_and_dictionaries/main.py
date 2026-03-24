"""main file to run functions library"""
import functions as f

def main():
    """program entry: calling environment to user-defined functions."""
    # initialize variables
    your_emails = []
    your_phones = []

    # function calls
    f.get_requirements()
    your_emails = f.add_emails()

    # use for testing return values
    # print(len(your_emails), your_emails)
    # exit()

    if len(your_emails) == 0:
        print("No emails!")
    else:
        your_phones = f.get_phones(your_emails)
        # testing returns
        # print(your_phones)
        # exit()

        f.create_contact(your_emails, your_phones)
    

if __name__ =="__main__":
    main()