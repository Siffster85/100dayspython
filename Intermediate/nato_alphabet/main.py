import pandas

#student_dict = {
#    "student": ["Angela", "James", "Lily"], 
#    "score": [56, 76, 98]
#}

#Looping through dictionaries:
#for (key, value) in student_dict.items():
    #Access key and value
    #pass

#student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
#for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    #pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

nato_df = pandas.read_csv("./Intermediate/nato_alphabet/nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

to_translate = input("What would you like to convert to the NATO alphabet?: ").upper() 
nato_list = [nato_dict[letter] for letter in to_translate]
print(nato_list)
