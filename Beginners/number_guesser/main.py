import random
from os import system
import art

print(art.logo)
print("Welcome to Guess That Number!")

def clear():
  system("clear||cls")

EASY_LEVEL_GUESSES = 10
HARD_LEVEL_GUESSES = 5

def set_difficulty():
  difficulty = input("Choose your difficulty! Type 'easy' or 'hard': ").lower()
  if difficulty == "easy":
    return EASY_LEVEL_GUESSES
  else:
    return HARD_LEVEL_GUESSES
  
def check_answer(guess, number, guesses):
  if guess < number:
    print("Too Low.")
    return guesses - 1
  elif guess > number:
    print("Too high.")
    return guesses - 1

def continue_playing():
  again = input("Would you like to play again? 'y' or 'n': ").lower()
  if again == "y":
    clear()
    game()
  else:
    clear()
    print("Thanks for playing! Bye!")

def game():
  number = random.randint(1,100)
  print("I'm thinking of a number between 1 and 100.")
  guesses = set_difficulty()
  guess = 0
  while guess != number:
    print(f"Your have {guesses} remaining to Guess That Number!:")
    guess = int(input("Make a guess: "))
    guesses = check_answer(guess, number, guesses)
    if guesses == 0:
      print(f"I'm sorry you're out of guesses, the correct answer was {number}")
      continue_playing()
  print(f"Congratulations! {number} is correct!")
  continue_playing()

game()
