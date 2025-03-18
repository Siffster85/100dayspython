from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

javabot = CoffeeMaker()
cashbot = MoneyMachine()
menubot = Menu()

def coffee_machine():
  
  request = input("What would you like? Espresso: $1.50, Latte: $2.50, Cappuccino: $3.00: ").lower()
  if request == "off":
    return
  elif request == "report":
    javabot.report()
    cashbot.report()
    coffee_machine()
  else:
    order = menubot.find_drink(request)
    if javabot.is_resource_sufficient(order):
      if cashbot.make_payment(order.cost):
        javabot.make_coffee(order)
    coffee_machine()

coffee_machine()
