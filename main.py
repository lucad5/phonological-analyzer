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

def create_environments_spreadsheet(dictionary_of_environments, output_filename):
    print("Placeholder")

    environments_file_created = False
    while environments_file_created != True:
        print("Placeholder")

    # TODO:
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

def determine_environments_of_segments(df_from_csv):

    # TODO: Function WIP
    ''' This will generate a dictionary with this structure (this example is based on an input consisting of the string "aa"):
    ["a": [{"pre-segment segment": "#", "post-segment segment": "#"}, {"pre-segment segment": "a", "post-segment segment": "#"}]}'''

    environments = {}

    csv_headers = list(df_from_csv)

    header_input_message = "\nThe file has the following columns (the column name/header is in parentheses):\n"

    for header_number, header_index in enumerate(csv_headers):
        column_header = "(%s)" % header_index

        header_input_message += "%s %s\n" % (column_header, header_number)

    header_input_message += "\nPlease type in the name/header of the column that contains the IPA transcription data: "

    valid_letter_entered = False
    while valid_letter_entered == False:
        try:
            letter_of_column_with_data = input(header_input_message)
    #    print(df_from_csv[letter_of_column_with_data].values[0])
            for content_of_cell in df_from_csv[letter_of_column_with_data].values:

                for char_index, char in enumerate(content_of_cell):

                    if char == " ":
                        continue

                    char_is_at_start_of_word = (char_index == 0 or content_of_cell[char_index-1] == " ")
                    if char_is_at_start_of_word:
                        character_before_character = "#"
                    else:
                        character_before_character = content_of_cell[char_index-1]

                    word_is_one_character = (len(content_of_cell) == 1)
                    char_is_at_end_of_word = (char_index == len(content_of_cell)-1 or content_of_cell[char_index+1] == " ")

                    if word_is_one_character or char_is_at_end_of_word:
                        character_after_character = "#"
                    else:
                        character_after_character = content_of_cell[char_index+1]
                    
                    environment_of_char = character_before_character + "_" + character_after_character

                    if char in environments:
                        if environment_of_char not in environments[char]:    
                            environments[char].append(environment_of_char)
                        else:
                            continue
                    elif char not in environments:
                        environments[char] = []
                        environments[char].append(environment_of_char)

            valid_letter_entered = True

        except KeyboardInterrupt: 
            print("\n\nKeyboard interrupt detected. Exiting.")
            break

        except:
            print("The input was not valid. Please try again.\n")
            continue

    return environments

def check_if_csv_has_header(csv_filename):

    try:
        with open(csv_filename, 'r') as f:

            csv_contents = f.readlines()

            # Test if the first row of the .csv file is valid (if it is a header)
            try:
                sample = csv_contents[0]
                has_header = csv.Sniffer().has_header(sample)
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

    input_file_opened = False
    while input_file_opened == False:

        filename = input("Please enter the name of the .csv file with the phonetic data you wish to analyze: ")
        
        if check_if_csv_filename_is_valid(filename) == False:
            print("Error: The file provided is does not end in '.csv.' Please try again.\n")
            continue
        
        csv_has_header = check_if_csv_has_header(filename)
        if csv_has_header == False:
            continue

        df_environments = pd.read_csv(filename)

        input_file_opened = True

    dictionary_of_environments = determine_environments_of_segments(df_environments)

    output_file_created = False
    while output_file_created == False:

            output_filename = input("\nPlease enter the filename you wish to use for the .csv file that will contain the aligned environments (note: the filename must end in \".csv\" (no quotes)): ")
            
            if check_if_csv_filename_is_valid(output_filename) == False:
                print("Error: The file provided is does not end in '.csv.' Please try again.")
                continue            

            if os.path.isfile(directory_of_main_py + "\\" + output_filename):
                print("Error: The file already exists. Please choose another filename.")
                continue

            create_environments_spreadsheet(dictionary_of_environments, output_filename)

            output_file_created = True

    print("The phonological environments from %s have been written to the file %s. Program execution complete.")




if __name__ == "__main__":
    main()