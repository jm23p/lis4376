"""main file to run functions library"""
import functions as f

def main():
    """function to pull from function library"""
    f.get_requirements()
    your_tuple = f.get_tuple()
    f.unpack_tuple(your_tuple)
    f.count_tuple(your_tuple)
    f.parse_tuple(your_tuple)
    f.reassign_tuple(your_tuple)
    f.remove_tuple(your_tuple)

if __name__ == "__main__":
    main()