import pandas  # import pandas for CSV reading
#TODO 1. Create a dictionary in this format:
letter_df = pandas.read_csv("nato_phonetic_alphabet.csv")  # load the NATO alphabet CSV into a dataframe

letter_df_dict = {row.letter:row.code for (index, row) in letter_df.iterrows()}  # build a dict mapping each letter to its NATO code word

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name = input("What name do you want spelt?").upper()  # get user input and convert to uppercase
output_list = [letter_df_dict[letter] for letter in name]  # look up the NATO word for each letter in the name

print(output_list)  # print the list of NATO code words
