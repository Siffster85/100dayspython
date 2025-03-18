MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def check_resources(ingredients, beverage):
  for ingredient, quantity in beverage.items():
    if ingredients[ingredient] < quantity:
      print(f"Sorry not enough {ingredient}.")
      coffee_machine()
  return True

def make_drink(ingredients, beverage):
  for ingredient, quantity in beverage.items():
    ingredients[ingredient] -= quantity
  
def payment(cost):
  print("Please insert coins:")
  quarters = int(input("Please insert Quarters: "))
  dimes = int(input("Please insert Dimes: "))
  nickles = int(input("Please insert Nickles: "))
  pennies = int(input("Please insert Pennies: "))
  
  total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
  
  if cost > total:
    print(f"Sorry, that's not enough money. {total} refunded.")
    coffee_machine()
  else:
    resources["money"] += cost
    difference = round(total - cost, 2)
    print(f"Processing your beverage now. {difference} in change.")
    return True
def print_report():
  print(f" Water: {resources["water"]}ml\n Milk: {resources["milk"]}ml\n Coffee: {resources["coffee"]}g\n Money: ${resources["money"]}")
  
def coffee_machine():
  request = input("What would you like? Espresso: $1.50, Latte: $2.50, Cappuccino: $3.00: ").lower()
  if request == "off":
    return
  elif request == "report":
    print_report()
    coffee_machine()
  else:
    available = check_resources(resources, MENU[request]["ingredients"])
    if available:
      paid = payment(MENU[request]["cost"])
      if paid:
        make_drink(resources, MENU[request]["ingredients"])
        print(f"Your {request} has been made, enjoy.")
        coffee_machine()

coffee_machine()
