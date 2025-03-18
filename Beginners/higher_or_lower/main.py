import random
from os import system
import art
import data

def clear():
  system("clear||cls")

def higher_or_lower():
  last_10_accounts = []
  high_score = 0
  
  def choose_account():
    if len(last_10_accounts) >= 10:
      last_10_accounts.pop(0)
    num = random.randint(0,49)
    while num in last_10_accounts:
      num = random.randint(0,49)
    last_10_accounts.append(num)
    return num
  
  def compare_accounts(account_a, account_b, guess):
    followers_a = data.data[account_a]['follower_count']
    followers_b = data.data[account_b]['follower_count']
    
    if followers_a == followers_b:
      print("It's a draw, lets carry on")
      return True
    else:
      if followers_a > followers_b:
        return guess == "A"
      else:
        return guess == "B"
      
  def game():
    nonlocal high_score
    clear()
    score = 0
    alive = True
    while alive:
      print(art.logo)
      if score == 0:
        account_a = choose_account()
        account_b = choose_account()
        print(f"Your score is {score}. Good Luck!")
      else:
        account_a = account_b
        account_b = choose_account()
        print(f"Correct! Your score is {score}!")
      print(last_10_accounts)
      print(account_a, account_b)
      char_a = data.data[account_a]
      char_b = data.data[account_b]
      
      print(f"Compare A: {char_a['name']}, a {char_a['description']}, from {char_a['country']}")
      print(art.vs)
      print(f"Against B: {char_b['name']}, a {char_b['description']}, from {char_b['country']}")
      
      guess = input("Who has more instgram followers? Type 'A' or 'B': ").upper()
      alive = compare_accounts(account_a, account_b, guess)
      if alive:
        score += 1
      clear()
    print(art.logo)
    if score > high_score:
      high_score = score
    print(f"I'm sorry, that's wrong, your final score is {score}")
    play_again = input("Would you like to play again? 'y' or 'n': ")
    if play_again == 'y':
      game()
    else:
      print(f"Thanks for playing, your highest score was {high_score}")

  game()
higher_or_lower()
