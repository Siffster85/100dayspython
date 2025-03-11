print("Welcome to the tip calculator!")
bill = int(input("How much is the bill? £"))
party = int(input("How many people is the bill being split between? "))
tip = int(input("What percentage tip do you want to give? "))

tip_amount = bill * (tip / 100)

equal_share = (bill + tip_amount) / party

to_pay = round(equal_share, 2)
formatted_to_pay = "{:.2f}".format(to_pay)

print(f"Each person needs to pay £{formatted_to_pay}")
