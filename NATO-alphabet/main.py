import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

error = True
while error:
    input_word = input("Enter word :")
    try:
        nato_list = [nato_dict[letter.upper()] for letter in list(input_word)]
    except KeyError:
        print("Please enter all  the alphabets")
    else:
        error = False
        print(nato_list)
