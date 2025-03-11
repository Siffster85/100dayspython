import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
       '''
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
          '''
          
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

result = "It's a draw!"

plays = [rock, paper, scissors]

player = int(input("SHOOT! Type '0' for Rock, '1' for Paper or '2' for scissors: "))
computer = random.randint(0, 2)

if player >= 3 or player < 0:
  print("I'm sorry, that's not an option.")
else:
  if player == 0 and computer == 2:
    result = "Congratulations! You win!"
  elif player == 2 and computer == 0:
    result = "Oh dear, you lose."
  elif player > computer :
    result = "Congratulations! You win!"
  elif player < computer:
    result = "Oh dear, you lose."
  elif player == computer:
    result = "It's a draw!"

  print(f"You've played:\n\n{plays[player]}")

  print(f"The Computer chose:\n\n{plays[computer]}")

  print(result)