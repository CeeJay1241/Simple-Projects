import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

turtle = turtle.Turtle()
turtle.hideturtle()
turtle.color("black")
turtle.penup()

num_chosen_states = 0
def choose_state():
    global answer_state
    answer_state = (screen.textinput(title="Guess the State", prompt=f"{num_chosen_states}/50 What's another state's name?")).lower()
    return answer_state

data = pandas.read_csv("50_states.csv")
data_list = data.state.to_list()
data_list = [i.lower() for i in data_list]
choose_state()

while num_chosen_states < 50:
    if answer_state in data_list:
        num_chosen_states +=1
        state_info = data[data.state == answer_state.capitalize()]
        turtle.goto(x=int(state_info["x"].iloc[0]), y=int(state_info["y"].iloc[0]))
        turtle.write(answer_state.capitalize(), align="center", font=("Arial", 8, "normal"))
        print(state_info)
        data_list.remove(answer_state)
        choose_state()
    else:
        choose_state()

turtle.mainloop()
