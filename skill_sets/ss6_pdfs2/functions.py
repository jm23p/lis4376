import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, 'titanic.csv')

df = pd.read_csv(csv_path)

def get_requirements():
    """function prints program requirements"""
    print("Pandas DataFrames and Series Structures")
    print("\nProgram Requirements:\n"
          + "Developer: Joshua Mann\n"
          + "1. Working with pandas DataFrames and Series data structures, for tabular data handling."
          + "2. DataFrame: Two-dimensional labeled data structure (i.e., rows/cols)."
          + "3. DataFrame: Series collection. Each column is Series sharing same index."
          + "4. Using multiple conditions: not, and, or."
          + "5. Logical operators, numeric comparisons, counting/comparing NaN/non-NaN values.")
    print("\nNote: not, and, or statements require truth-values.")
    print("\nPandas requires \"bitwise\" (overloaded operators): not (~), and (&), or (|).")

def display_pandas_and_data():
    print("\nPrint pandas version:")
    print(pd.__version__)

    print("\nDisplay data:")
    print(df)

def display_types():
    print("\nDisplay type:")
    print(type(df))

    print("\nTotal number of passengers:", len(df)) # displays length of passenger list, i.e. how many there were total

    perished = len(df[df['survived'] == 'no']) # runs through length of survived column; if no, add to perished total
    print("\nTotal number perished:", perished)

    males_perished = len(df[(df['survived'] == 'no') & (df['gender'] == 'male')]) # if passenger both didnt survive and is male, add to males_perished
    print("\nTotal males perished:", males_perished)

    males_perished_percent = (males_perished / perished) * 100 # divide amount of males perished to total perished
    print("\nPercentage of males who died from total perished: " + str(format(males_perished_percent, ".2f")) + "%")

    age_above_seventy_below_five = len(df[(df['age'] > 70) | (df['age'] < 5)]) # if passenger's age is above 70 or below 5, add to variable
    print("\nTotal number of passengers older than 70 OR younger than 5:", age_above_seventy_below_five)

    unique_homecountry = df['country'].nunique(dropna=False) # sifts through country column, nunique() checks for unique values, dropna=False includes the NaN values per instruction
    print("\nTotal number of unique home countries:", unique_homecountry)

    unique_homecountry_exclude = df[~df['country'].isin(['England', 'France'])]['country'].nunique(dropna=False) # same as above, but
    # adds condition to exclude values within country column if the value is England or France:
    # ~ means not, and .isin checks each element in the country column
    print("\nTotal number of unique home countries, not including England or France:", unique_homecountry_exclude)