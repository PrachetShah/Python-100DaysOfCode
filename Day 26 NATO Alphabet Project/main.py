import pandas


#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# data_frame = pandas.DataFrame(data)
dict = {row.letter: row.code for (index, row) in data.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ")
new_word = word.upper()
print(new_word)
phonetic_list = [dict[letter] for letter in new_word]
print(phonetic_list)