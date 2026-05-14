import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

num_chosen_states = 0

data = pandas.read_csv("50_states.csv")
data_list = data.state.to_list()
data_list = [i.lower() for i in data_list]
answer_state = screen.textinput(title="Guess the State", prompt=f"{num_chosen_states}/50 What's another state's name?")

while num_chosen_states < 50:
    if answer_state in data_list:
        num_chosen_states +=1
        data_list.remove(answer_state)
        answer_state = screen.textinput(title="Guess the State", prompt=f"{num_chosen_states}/50What's another state's name?")
    else:
            answer_state = screen.textinput(title="Guess the State", prompt=f"{num_chosen_states}/50What's another state's name?")



turtle.mainloop()