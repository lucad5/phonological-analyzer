# phonological-analyzer
Given a .csv file, determines the phonological environment of each character in a dataset.

# Instructions
- Run `python main.py`
- Type the name of the .csv file in the current directory you wish to analyze (if you do not have one, you can type `example.csv`), and press Enter
- Type the number of the column that contains the IPA data (if you used the example.csv file, type `1`), and press Enter
- Type the desired name for the output .csv file that will contain the aligned environments for each segment, and press Enter

# Functionality
- Takes a .csv file as input, and outputs a separate .csv file that contains the environments for each segment in a column in the .csv file
- Provides the environments in aligned format, to see at a glance which segments have shared environments

# Feature wishlist
- Provide suggestions as to which segments may be in complementary distribution, contrastive distribution, or free variation
- Provide a condensed summary of the different types of environments (e.g. interconsonantal, intervocalic, word-initial, word-final) segments occur in.
  - For example, given a dataset where `e` occurs in the environments `#_d` and `f_#` the environments for `e` could be summarized as:
  - `word-initial: #_d` <br /> `word-final: f_#`
- Sort the segments and environments in the output .csv file in alphabetical order
