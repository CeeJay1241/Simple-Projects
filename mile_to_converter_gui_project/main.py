from tkinter import *  # import all tkinter widgets

def miles_to_km():  # function called when the calculate button is clicked
    miles = float(miles_input.get())  # get the value from the input field and convert to float
    km = miles * 1.609  # convert miles to kilometers
    kilometer_result_label.config(text=f"{km}")  # update the result label with the converted value

window = Tk()  # create the main application window
window.title("Miles to Kilometer")  # set the window title
window.config(padx=20, pady=20)  # add padding around the window contents

miles_input = Entry(width=7)  # create a text entry field for miles input
miles_input.grid(column=1, row=0)  # place the entry field in the grid

miles_label = Label(text="Miles")  # create a label reading "Miles"
miles_label.grid(column=2, row=0)  # place the label to the right of the input

is_equal_label = Label(text="is equal to")  # create a label reading "is equal to"
is_equal_label.grid(column=0, row=1)  # place it on the left of the second row

kilometer_result_label = Label(text="0")  # create a label to display the km result, defaulting to 0
kilometer_result_label.grid(column=1, row=1)  # place it in the center of the second row

kilometer_label = Label(text="Km")  # create a label reading "Km"
kilometer_label.grid(column=2, row=1)  # place it to the right of the result

calculate_button = Button(text="Calculate", command=miles_to_km)  # create a button that triggers the conversion
calculate_button.grid(column=1, row=2)  # place the button below the result row

window.mainloop()  # start the tkinter event loop to keep the window open