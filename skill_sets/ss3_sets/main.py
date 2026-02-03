"""main file to run functions library"""
import functions as f

def main():
    """docstring goes here just talk about it"""
    f.get_requirements()
    your_set = f.get_set()
    f.get_other_sets()
    f.count_set(your_set)
    f.add_set(your_set)
    f.update_set(your_set)
    f.discard_element(your_set)
    f.remove_element(your_set)
    f.min_element(your_set)
    f.max_element(your_set)
    f.sum_elements(your_set)
    f.clear_set(your_set)

if __name__ =="__main__":
    main()