print('''
      *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to avoid death and hopefully find treasure!")
choice1 = input("You're at a crossroads, which way would you like to go?\nType 'left' or 'right' to decide: ").lower()

if choice1 == "left":
  choice2 = input("Congratulations, you safely make it to the beach, you can see the island across the water.\nType 'wait' to wait for a boat or type 'swim' to swim over to the island: ").lower()
  if choice2 == "wait":
    choice3 = input("A boat arrives and safely ferries you to the island.\nYou find 3 doors, do you go through 'red' 'yellow' or 'blue' ? ").lower()
    if choice3 == "yellow":
      print("Congratulations, you found the treasure.")
    elif choice3 == "blue":
      print("Oh dear, you're eaten by a Grue. GAME OVER!")
    elif choice3 == "red":
      print("Oh dear, you fell into lava. GAME OVER!")
    else:
      print("Wrong input, game over")
  elif choice2 == "swim":
    print("Oh dear, you were eaten by a shark. GAME OVER!")
  else:
      print("Wrong input, game over")
elif choice1 == "right":
  print("You fall into a hole and die. GAME OVER!")
else:
  print("Wrong input, game over")
