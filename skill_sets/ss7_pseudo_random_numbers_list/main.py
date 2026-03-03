"""main file to run functions library"""
import functions as f

def main():
    """function to pull from function library"""
    # initialize variable(s)
    f.get_requirements()
    size = f.get_list_size()
    # use below for unit testing
    # print(size)
    # exit()
    your_list = f.create_list(size)
    # print(your_list) # check pseudo-random number list
    f.sort_list(your_list)
    

if __name__ =="__main__":
    main()