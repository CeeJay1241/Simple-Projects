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
    response = screen.textinput(title=f"{num_chosen_states}/50 States Correct", prompt="What's another state's name?")
    answer_state = response.title() if response is not None else "Exit"
    return answer_state

data = pandas.read_csv("50_states.csv")
data_list = data.state.to_list()
#data_list = [i.lower() for i in data_list]
choose_state()

while num_chosen_states < 50:
    if answer_state == "Exit":
        break

    if answer_state in data_list:
        num_chosen_states +=1
        state_info = data[data.state == answer_state]
        turtle.goto(x=int(state_info["x"].iloc[0]), y=int(state_info["y"].iloc[0]))
        turtle.write(answer_state, align="center", font=("Arial", 8, "normal"))
        print(state_info)
        data_list.remove(answer_state)
        choose_state()
    else:
        choose_state()
        
forgotten_states = pandas.DataFrame(data_list)
forgotten_states.to_csv("states_to_learn.csv")