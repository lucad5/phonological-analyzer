import os
import pandas as pd
import csv
from pathlib import Path

def check_if_csv_filename_is_valid(filename):

    if filename.endswith('.csv'):
        return True

    elif filename.endswith('.csv') == False:
        return False

def create_environments_spreadsheet(dictionary_of_environments, output_filename):

    # This is to create a list of unique environments that will be used to align the environments in the spreadsheet
    list_of_unique_environments = []
    for character in dictionary_of_environments:
         for environment in dictionary_of_environments[character]:
             if environment not in list_of_unique_environments:
                 list_of_unique_environments.append(environment)
             else:
                 continue

    number_of_unique_environments = len(list_of_unique_environments)

    try:
        with open(output_filename, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            first_row = ["Segments:"] + list_of_unique_environments
            writer.writerow(first_row)
            
            for segment_index, (segment, segment_environments) in enumerate(dictionary_of_environments.items()):
                current_line = [segment]

                for unique_environment_index, environment_from_list_of_unique_environments in enumerate(list_of_unique_environments):
                    if environment_from_list_of_unique_environments in segment_environments:
                        current_line.append(environment_from_list_of_unique_environments)
                    else:
                        current_line.append("")
                writer.writerow(current_line)
    except:
        print("An error occurred. Exiting.")

def determine_environments_of_segments(df_from_csv):

    ''' This will generate a dictionary with this structure (this example is based on an input consisting of the string "aa"):
    ["a": ["#_a", "a_#"]}'''

    environments = {}

    csv_headers = list(df_from_csv)

    header_input_message = "\nThe file has the following columns (the column name/header is after the parentheses):\n"

    headers_and_their_numbers = {}

    for header_number, header_name in enumerate(csv_headers):
        headers_and_their_numbers[header_number] = header_name

        header_input_message += "(%d) %s\n" % (header_number, header_name)

    header_input_message += "\nPlease type in the number (shown in parentheses) of the column that contains the IPA transcription data: "

    valid_number_entered = False
    while valid_number_entered == False:
        try:
            number_of_column_with_data = int(input(header_input_message))
            name_of_column_with_data = headers_and_their_numbers[number_of_column_with_data]

            for content_of_cell in df_from_csv[name_of_column_with_data].values:

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

            valid_number_entered = True

        except KeyboardInterrupt: 
            print("\n\nKeyboard interrupt detected. Exiting.")
            quit()

        except:
            print("The input was not valid. Please try again.\n")
            continue

    return environments

def check_if_csv_has_header(csv_filename):

    try:
        with open(csv_filename, 'r', encoding="utf-8") as f:

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

    valid_file_provided = False
    while valid_file_provided == False:

        filename = input("Please enter the name of the .csv file with the phonetic data you wish to analyze: ")
        
        if check_if_csv_filename_is_valid(filename) == False:
            print("Error: The file provided is does not end in '.csv.' Please try again.\n")
            continue
        
        csv_has_header = check_if_csv_has_header(filename)
        if csv_has_header == False:
            continue

        valid_file_provided = True

    df_environments = pd.read_csv(filename, encoding='utf-8')
    dictionary_of_environments = determine_environments_of_segments(df_environments)

    output_file_created = False
    while output_file_created == False:

            output_filename = input("\nPlease enter the filename you wish to use for the .csv file that will contain the aligned environments (note: the filename must end in \".csv\" (no quotes)): ")
            
            if check_if_csv_filename_is_valid(output_filename) == False:
                print("Error: The file provided does not end in '.csv.' Please try again.")
                continue            

            if os.path.isfile(directory_of_main_py + "\\" + output_filename):
                print("Error: The file already exists. Please choose another filename.")
                continue

            create_environments_spreadsheet(dictionary_of_environments, output_filename)

            output_file_created = True

    print("Success! The phonological environments from %s have been written to the file %s. Exiting program." % (filename, output_filename))

if __name__ == "__main__":
    main()