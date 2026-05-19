import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"  # path to the blank US map image
screen.addshape(image)
turtle.shape(image)

turtle = turtle.Turtle()
turtle.hideturtle()
turtle.color("black")
turtle.penup()  # lift pen so moving doesn't draw lines

num_chosen_states = 0  # tracks correct guesses
def choose_state():
    global answer_state  # allows the function to modify the outer variable
    response = screen.textinput(title=f"{num_chosen_states}/50 States Correct", prompt="What's another state's name?")
    answer_state = response.title() if response is not None else "Exit"  # title-case input, or "Exit" if dialog was cancelled
    return answer_state

data = pandas.read_csv("50_states.csv")
data_list = data.state.to_list()  # list of remaining unguessed states
choose_state()

while num_chosen_states < 50:
    if answer_state == "Exit":  # user cancelled the dialog
        break

    if answer_state in data_list:
        num_chosen_states += 1
        state_info = data[data.state == answer_state]  # filter dataframe to matching state row
        turtle.goto(x=int(state_info["x"].iloc[0]), y=int(state_info["y"].iloc[0]))  # iloc[0] extracts scalar from Series
        turtle.write(answer_state, align="center", font=("Arial", 8, "normal"))
        print(state_info)
        data_list.remove(answer_state)
        choose_state()
    else:
        choose_state()

forgotten_states = pandas.DataFrame(data_list)  # create dataframe from remaining unguessed states
forgotten_states.to_csv("states_to_learn.csv")  # save missed states to CSV for later review
