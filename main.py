import turtle
import pandas

screen = turtle.Screen()
screen.title("Nigerian states game")
image = "nigerian_map.gif"
screen.addshape(image)
turtle.shape(image)
screen.cv._rootwindow.resizable(False, False)
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

STATES_FILE = "list_of_states_in_nigeria.csv"

data = pandas.read_csv(STATES_FILE)
list_of_states = data['states'].to_list()
correct_guesses = []
while len(correct_guesses) < 37:
    user_guess =  screen.textinput(title=f"{len(correct_guesses)}/37 guessed", prompt="Guess the next state").title()
    if user_guess == "Exit" or len(correct_guesses) == 37:
        break
    if user_guess in list_of_states:
        state = data[data['states'] == user_guess ]
        x_cor = int(state.x)
        y_cor = int(state.y)
        correct_guesses.append(user_guess)

        writer.goto(x_cor, y_cor)
        writer.write(user_guess)


missing_states = [state  for state in list_of_states if state not in correct_guesses]
# for state in list_of_states:
#     if state not in correct_guesses:
#         missing_states.append(state)

data_for_missing_states = pandas.DataFrame(missing_states)
data_for_missing_states.to_csv("states_to_practice")


