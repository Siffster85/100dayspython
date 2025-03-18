import random
import hangman_art
from hangman_words import word_list

chosen_word = random.choice(word_list)

display = []
lives = 6
guesses = []

for l in chosen_word:
  display.append("_")

game_won = False
game_lost = False

print(hangman_art.logo)
while not game_won and not game_lost:
  print(hangman_art.stages[lives])
  print(f"{' '.join(display)}")
  if len(guesses) > 0:
    print(f"You have tried: {' '.join(guesses)}")
  
  guess = input("Guess a letter\n").lower()

  for index, l in enumerate(chosen_word):
    if l == guess:
      display[index] = guess
  if guess in guesses or guess in display:
    print("You've already tried that, try again.")
  else:
    if guess not in chosen_word:
      guesses.append(guess)
      print(f"I'm sorry, {guess} is incorrect")
      lives -= 1
    if lives == 0:
      game_lost = True
  if "_" not in display:
    game_won = True
  

if game_won == True:
  print(f"You win! The word was {chosen_word}")
elif game_lost == True:
  print(hangman_art.stages[lives])
  print(f"You lose! The word was {chosen_word}")

