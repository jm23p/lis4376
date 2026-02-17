"""main file to run functions library"""
import functions as f

def main():
    """function to pull from function library"""
    f.get_requirements()
    your_dictionary = f.get_dictionary()
    f.parse_dictionary(your_dictionary)
    f.count_dictionary(your_dictionary)
    f.add_element(your_dictionary)
    f.update_element(your_dictionary)
    f.delete_element(your_dictionary)
    f.delete_dictionary(your_dictionary)

if __name__ =="__main__":
    main()