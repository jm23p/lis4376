import functions as f

def main():
    """docstring goes here just talk about it"""
    f.get_requirements()
    your_list = f.get_list1()
    your_list = f.add_list1(your_list)
    f.count_list1(your_list)
    f.reverse_list1(your_list)
    f.remove_list1(your_list)

    # create new list for sorting
    new_list = f.get_list2()
    f.sort_list2(new_list)

if __name__ =="__main__":
    main()