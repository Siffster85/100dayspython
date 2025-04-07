import turtle
import pandas

FONT = ('Arial', 8, 'normal')

screen = turtle.Screen()

screen.title("U.S. States Game")
image = "./Intermediate/us_states_game_start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
timo = turtle.Turtle()
timo.ht()
timo.pu()

correct_guesses = []

states = pandas.read_csv("./Intermediate/us_states_game_start/50_states.csv")
states_list = states.state.to_list()

def write_answer_location(state_string):
  state_details = states[states.state == state_string]
  timo.goto(int(state_details.x), int(state_details.y))
  timo.write(state_details.state.item(), align="left", font=FONT)


while len(correct_guesses) < 50:
  if len(correct_guesses) > 0:
    title = f"{len(correct_guesses)}/50 States correct"
  else:
    title = "Guess the States"
    
  answer_state = screen.textinput(title=title, prompt="What's your guess?").title()
  if answer_state == "Exit":
    states_to_learn = [state for state in states_list if state not in correct_guesses]
    state_dataframe = pandas.DataFrame(states_to_learn)
    state_dataframe.to_csv("./Intermediate/us_states_game_start/states_to_learn.csv")
    break
  
  if answer_state in states_list and answer_state.title() not in correct_guesses:
    correct_guesses.append(answer_state)
    write_answer_location(answer_state)
    




screen.exitonclick()