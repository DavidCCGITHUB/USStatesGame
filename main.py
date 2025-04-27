import turtle
import pandas

from states import States

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states = States()

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f" {len(states.successful_list)}/{len(states.states_list)} States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [missing_state for missing_state in states.states_list if missing_state not in states.successful_list]
        states_to_learn = {"states missed": missing_states}
        data = pandas.DataFrame(states_to_learn)

        data.to_csv("states_to_learn.csv")
        break

    states.check_state(answer_state)




screen.exitonclick()