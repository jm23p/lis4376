"""main file to run functions library"""
import functions as f

def main():
    """function to pull from function library"""
    f.get_requirements()
    f.get_data()
    my_bool = f.get_bool_data()
    f.count_bool_cols(my_bool)
    f.count_bool_rows(my_bool)
    f.count_bool_total(my_bool)
    my_series = f.get_series_data()
    f.evaluate_series_data(my_series)
    f.convert_dataframe_to_numpy_array(my_bool)

if __name__ =="__main__":
    main()