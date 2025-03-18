import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)
def begin():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  if direction == "encode" or direction == "decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    def caeser(start_text, shift_input, cipher_direction):
      shift_amount = shift_input % 26
      
      if cipher_direction == "decode":
        shift_amount *= -1
      ciphered = ""
      
      for char in start_text:
        if char in alphabet:
          for index, l in enumerate(alphabet):
            if l == char:
              shifted = index + shift_amount
              if shifted > 25:
                ciphered += alphabet[shifted - 26]
              elif shifted < 0:
                ciphered += alphabet[shifted + 26]
              else:
                ciphered += alphabet[shifted]
        else:
          ciphered += char
      print(f"The {cipher_direction}d text is {ciphered}")
      
    caeser(start_text=text, shift_input=shift, cipher_direction=direction)
      
    cipher = input("Would you like to continue? 'yes' or 'no'\n").lower()
    if cipher == "yes":
      begin()
    else:
      print("Goodbye")
  else:
    print("Incorrect command, please try again.")
begin()
