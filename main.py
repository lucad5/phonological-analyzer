# The following contains both code (in progress), as well as pseudocode that will be rewritten using real code

import os
import magic
import pandas as pd
import csv
from pathlib import Path

def check_if_csv_filename_is_valid(filename):

    if filename.endswith('.csv'):
        return True

    elif filename.endswith('.csv') == False:
        return False

def determine_environments_of_segments(columns_from_csv):

    # TODO: Function WIP
    # TODO: Ask what the separator for the csv will be
    ''' This will generate a dictionary with this structure (this example is based on an input consisting of the string "aa"):
    ["a": [{"pre-segment segment": "#", "post-segment segment": "#"}, {"pre-segment segment": "a", "post-segment segment": "#"}]}'''

    environments = {}

    headers = columns_from_csv[0].rstrip("\n").split(",")

    print(headers)
#    for row in columns_from_csv:
#        headers.append(row.split(","))
#        print(headers)


    # Extract column names from .csv file (i.e., the text in the first row for each column) and put each column name into a dictionary
    # Print "The file [example.csv] has the following columns:
    # A title
    # B title2
    # C title3
    # Please type in the letter of the column that contains the IPA text"

    # for cell in column: 

    # #  TODO: this should use an index, not a for loop
    #   for character in cell

    #       if character_index == 0 or character[index-1] == " ":
    #           character_before_character = "#"
    #       else:
    #           character_before_character = cell[character_index+1]

    #       if character_index == cell.length():
    #           character_after_character = "#"
    #       else:
    #           character_after_character = cell[character_index+1]
        

    #       environment = character_before_character + "_" + character_after_character

    #       if character in environments_of_characters:
    #           if environment not in environments_of_characters[character]:    
    #               characters_and_environments[character].append(environment)
    #           else:
    #               continue

    return environments



def check_if_csv_has_header(csv_filename):

    try:
        with open(csv_filename, 'r') as f:

            csv_contents = f.readlines()

            # Test if the first row of the .csv file is valid (if it is a header)
            try:
                sample = csv_contents[0]
                has_header = csv.Sniffer().has_header(sample)
                print(has_header)
                if has_header == False:
                    return False
                else:
                    return True
            except csv.Error:
                incorrect_formatting_error_message = "\nError: The first row of this .csv file is not formatted correctly." \
                    " It might be missing delimiters (like commas, spaces) between the cells." \
                    " Try again after resolving any issues with the first row of the file.\n"
                print(incorrect_formatting_error_message)
                return False
    except IOError:
        print('Error: There was an error opening the file %s\n' % filename)
        return False
 
    return False   

def main():

    directory_of_main_py = os.path.dirname(os.path.abspath(__file__))
    os.chdir(directory_of_main_py)

    file_opened = False
    while file_opened == False:

        filename = input("Please enter the name of the .csv file with the phonetic data you wish to analyze: ")
        
        if check_if_csv_filename_is_valid(filename) == False:
            print("Error: The file provided is does not end in '.csv.' Please try again.\n")
            continue
        
        csv_has_header = check_if_csv_has_header(filename)
        if csv_has_header == False:
            continue

        df_environments = pd.read_csv(filename)

        file_opened = True

#        dictionary_of_environments = determine_environments_of_segments(df_environments)


    # # TODO:

    # environments_file_created = False
    # while environments_file_created != True:
    #     input("Please enter the filename you wish to use for the .csv file where the phonological environments will be saved to (example: environments.csv): ")
    #     if filename does not exist in current folder
    #         create new file (environments.csv)
    #         environments_file_created = True
    #     elif filename exists:
    #         print("Error: A file with that filename already exists in the current directory.")
    #         continue

    # # this is for being able to align and sort the environments in the spreadsheet
    # list_of_unique_environments = []
    # for character in characters_and_environments:
    #     for environment in characters_and_environments[character]:
    #         if environment in list_of_unique_environments:
    #             list_of_unique_environments.append(environment)
    #         else:
    #             continue
            

    # sort elements in list_of_unique_environments alphabetically
    # number_of_unique_environments = list_of_unique_environments.length()

    # open environments_file

    # # align the environments in the spreadsheet using this sort of format
    # # (where each unique environment is in its own cell, and the cells are sorted horizontally based on the first character in the environment):
    # # k a_o
    # # c a_o #_o
    # # m         


    # # Add all unique environments to the first row to enable alignment
    # # Iterate over columns until there are no more unique environments
    # for environment_index in range(0, number_of_unique_environments):
        
    #     # add environment to a cell in a column in in the first row (don't know if this is how you iterate over columns)
    #     csv_file[environment_index] = list_of_unique_environments[environment_index]



    # add each character and its phonological environments to the spreadsheet
    # for current_row in environments_file:
    #     # 
    #     if current_row is the first row:
    #         continue

    #     # iterate over each cell in the row
    #     for cell in environments_file:
    #         for character, environments_of_character in environments_dictionary:
                
    #             add character to cell in first column
    #             # add environments of that character in subsequent columns
    #             for environment in environments_of_character:
    #                 compare environment to unique_environments in first row, to find which column the environment should be in
    #                 environment_column = column_of_environment_in_first_row
    #                 add environment to current_row[environment_column]


    # in the spreadsheet, remove placeholder unique environments from the first row
    # in the spreadsheet, add the string "Phonetic segment" to the cell in the first row in the first column 

if __name__ == "__main__":
    main()