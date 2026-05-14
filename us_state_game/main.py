import turtle  # import turtle graphics module
import pandas  # import pandas for CSV handling

screen = turtle.Screen()  # create the game window
screen.title("U.S. States Game")  # set the window title
image = "blank_states_img.gif"  # path to the blank US map image
screen.addshape(image)  # register the image as a turtle shape
turtle.shape(image)  # display the map as the background

turtle = turtle.Turtle()  # create a turtle for writing state names
turtle.hideturtle()  # hide the turtle cursor
turtle.color("black")  # set text color to black
turtle.penup()  # lift pen so moving doesn't draw lines

num_chosen_states = 0  # track how many states have been guessed correctly
def choose_state():  # function to prompt the user for a state guess
    global answer_state  # allow the function to modify the outer variable
    response = screen.textinput(title=f"{num_chosen_states}/50 States Correct", prompt="What's another state's name?")  # show input dialog
    answer_state = response.title() if response is not None else "Exit"  # title-case the input, or set "Exit" if dialog was cancelled
    return answer_state  # return the answer

data = pandas.read_csv("50_states.csv")  # load state names and coordinates from CSV
data_list = data.state.to_list()  # convert the state column to a plain list
#data_list = [i.lower() for i in data_list]
choose_state()  # get the first guess from the user

while num_chosen_states < 50:  # keep looping until all 50 states are guessed
    if answer_state == "Exit":  # stop the game if user cancels the dialog
        break

    if answer_state in data_list:  # check if the guess is a valid unguessed state
        num_chosen_states +=1  # increment the correct guess counter
        state_info = data[data.state == answer_state]  # look up the state's row in the dataframe
        turtle.goto(x=int(state_info["x"].iloc[0]), y=int(state_info["y"].iloc[0]))  # move turtle to the state's map coordinates
        turtle.write(answer_state, align="center", font=("Arial", 8, "normal"))  # write the state name on the map
        print(state_info)  # print the state info to the console
        data_list.remove(answer_state)  # remove the guessed state from the remaining list
        choose_state()  # prompt for the next guess
    else:
        choose_state()  # prompt again if the guess was wrong or already used

forgotten_states = pandas.DataFrame(data_list)  # create a dataframe from the remaining unguessed states
forgotten_states.to_csv("states_to_learn.csv")  # save the missed states to a CSV file
