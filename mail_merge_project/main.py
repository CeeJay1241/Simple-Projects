#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt", "r") as names_file:  # open the names file for reading
    names = names_file.readlines()  # read all lines into a list

with open("Input/Letters/starting_letter.txt", "r") as letter_file:  # open the template letter for reading
    string = letter_file.read()  # read the full letter content as a string
    for name in names:  # loop through each name
        stripped_name = name.strip()  # remove leading/trailing whitespace and newlines
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as letter:  # create the output file for this name
            new_string = string.replace("[name]", f"{stripped_name}")  # replace the [name] placeholder with the actual name
            letter.write(new_string.strip())  # write the personalized letter, stripping extra whitespace
