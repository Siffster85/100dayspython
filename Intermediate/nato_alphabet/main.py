import pandas

nato_df = pandas.read_csv("./Intermediate/nato_alphabet/nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_df.iterrows()}

def translate():
  to_translate = input("What would you like to convert to the NATO alphabet?: ").upper()
  try: 
    nato_list = [nato_dict[letter] for letter in to_translate]
  except KeyError:
    print("I'm afraid only letters are allowed, please try again.")
    translate()
  else:
    print(nato_list)

translate()
