import turtle
import prettytable

timo = turtle.Turtle()
table = prettytable.PrettyTable()

""" print(timo)
timo.shape("turtle")
timo.color("DarkSeaGreen4")
timo.fd(100)

my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick() """

table.field_names = [ "Pokemon Name", "Type" ]
table.align["Pokemon Name"] = "r"
table.align["Type"] = "l"
table.add_row(["Pikachu", "Electric"])
table.add_rows([
  ["Squirtle", "Water"],
  ["Charmander", "Fire"],
])

print(table)