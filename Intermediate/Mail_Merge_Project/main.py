#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        

def mail_merge():
  
  with open("./Intermediate/Mail_Merge_Project/Input/Names/invited_names.txt") as names:
    names_list = (names.readlines())
    
  with open("./Intermediate/Mail_Merge_Project/Input/Letters/starting_letter.txt") as letter:
    letter_form = letter.read()
    
  for name in names_list:
    recepiant = name.strip()
    personal_letter = letter_form.replace("[name]", recepiant)
    with open(f"./Intermediate/Mail_Merge_Project/Output/ReadyToSend/{recepiant}.txt", mode="w") as new_letter:
      new_letter.write(personal_letter)
  
mail_merge()