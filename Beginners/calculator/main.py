import art

print(art.logo)

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add, 
  "-": subtract, 
  "*": multiply, 
  "/": divide
}

def calculator():
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)

  should_continue = True

  while should_continue:
    operator = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculate_function = operations[operator]
    answer = calculate_function(num1, num2)

    print(f"{num1} {operator} {num2} = {answer}")
    response = input(f"Type 'y' to continue with {answer} or 'n' to start a new calculation or 'x' to exit: ").lower()
    if response  == "y":
      num1 = answer
    elif response  == "n":
      should_continue = False
      calculator()
    else:
      should_continue = False
      
calculator()
