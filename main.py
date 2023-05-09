import turtle
import pandas

screen = turtle.Screen()
data = pandas.read_csv("50_states.csv")
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
score = 0
location = turtle.Turtle()
location.penup()
location.hideturtle()
all_states = data.state.to_list()
guessed_state = []
while score < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States",
                                    prompt="What's another state name?").title()
    if answer_state.lower() == "exit":
        break
    if answer_state in all_states:
        if answer_state not in guessed_state:
            data_row = data[data.state == answer_state]
            guessed_state.append(answer_state)
            location.goto(int(data_row.x), int(data_row.y))
            location.write(arg=answer_state, move=False, align='center', font=("Arial", 14, 'normal'))

# for state in guessed_state:
#     all_states.remove(state)
#
# data_states_to_learn = pandas.DataFrame(all_states)
states_to_learn=[state for state in all_states if state not in guessed_state]

data_states_to_learn = pandas.DataFrame(states_to_learn)
data_states_to_learn.to_csv("states_to_learn.csv")

