import random
import art

print(art.logo)

def deal_card(hand):
  """Deals random card from deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  hand.append(card)
  
def game(): 
  """Starts blackjack game"""
  player_cards = []
  dealer_cards = []
  for _ in range(2):
    deal_card(player_cards)
    deal_card(dealer_cards)
    
  def another_game():
    if input("Play again? 'y' or 'n': ").lower() == "y":
      game()
    else:
      print("Thanks for playing!")
  
  if sum(player_cards) == 21 and sum(dealer_cards) != 21:
    print(f"Your Cards: {player_cards} Dealer: {dealer_cards} Total: {sum(dealer_cards)}")
    print("BLACKJACK! You win")
    another_game()
  elif sum(player_cards) == 21 and sum(dealer_cards) == 21:
    print(f"Your Cards: {player_cards} Dealer: {dealer_cards}")
    print("Draw, tough luck.")
    another_game()
  else:
    
    def ace_check(hand):
      """Checks for an Ace in busted hands and reduces ace to value 1"""
      for card in hand:
        if card == 11:
          hand.remove(card)
          hand.append(1)
          if hand == player_cards:
            player_turn()
          elif hand == dealer_cards:
            dealer_turn()
    
    def player_turn():
      """Starts the player turn and input loop"""        
      while sum(player_cards) < 21:
        if input(f"Your Cards: {player_cards} Totaling: {sum(player_cards)} Dealer Showing: {dealer_cards[0]}. \nTo hit type 'h' to stand 's': ").lower() == "h":
          deal_card(player_cards)
          if sum(player_cards) > 21:
            ace_check(player_cards)
        else:
          return sum(player_cards)
      return sum(player_cards)
        
    def dealer_turn():
      """Starts and returns the dealers turn"""
      while sum(dealer_cards) < 17:
        deal_card(dealer_cards)
        print(f"Your Score: {sum(player_cards)} Dealer Showing: {dealer_cards} Totalling: {sum(dealer_cards)}")
        if sum(dealer_cards) > 21:
          ace_check(dealer_cards)
      return sum(dealer_cards)
        
    def play_game():
      """Starts the game input loop and returns the result"""
      player_total = player_turn()
      if player_total > 21:
        print(f"Your Cards: {player_cards} Your Score: {player_total} Dealer Showing: {dealer_cards} Totalling: {sum(dealer_cards)}")
        print("Busted, you lose.")
      else:
        dealer_total = dealer_turn()
        if dealer_total > 21:
          print(f"Your Cards: {player_cards} Your Score: {player_total} Dealer Showing: {dealer_cards} Totalling: {dealer_total}")
          print("Dealer Busts! You Win!")
        elif dealer_total > player_total:
          print(f"Your Cards: {player_cards} Your Score: {player_total} Dealer Showing: {dealer_cards} Totalling: {dealer_total}")
          print("Dealer Wins")
        elif dealer_total < player_total:
          print(f"Your Cards: {player_cards} Your Score: {player_total} Dealer Showing: {dealer_cards} Totalling: {dealer_total}")
          print("Congratulations, you win!")
        else:          
          print(f"Your Cards: {player_cards} Your Score: {player_total} Dealer Showing: {dealer_cards} Totalling: {dealer_total}")
          print("Draw")
      another_game()
        
    play_game()
game()
