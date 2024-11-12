# The following contains both code (in progress), as well as pseudocode that will be rewritten using real code

import os
import magic
from pathlib import Path

def main():

    directory_of_main_py = os.path.dirname(os.path.abspath(__file__))
    os.chdir(directory_of_main_py)

    file_opened = False
    while file_opened == False:
        filename = input("Please enter the name of the .csv file with the phonetic data you wish to analyze: ")
        
        # TODO: add a check to see if the file exists
        if filename.endswith('.csv'):
            print("Success\n")
            continue

        elif filename.endswith('.csv') == False:
            print("The file provided is not a .csv file. Please try again.\n")
            continue


        file_opened = True

    #   check if filename exists
    #       check if file is .csv using the magic library
    #           if file is .csv, open .csv file
    #           file_opened = 1
    #   else:
    #       print "sorry, there is no file with that filename. Please try again"


    # characters_and_environments = {}
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