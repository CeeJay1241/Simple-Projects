import pandas
#TODO 1. Create a dictionary in this format:
letter_df = pandas.read_csv("nato_phonetic_alphabet.csv")

letter_df_dict = {row.letter:row.code for (index, row) in letter_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name = input("What name do you want spelt?").upper()
output_list = [letter_df_dict[letter] for letter in name]

print(output_list)
