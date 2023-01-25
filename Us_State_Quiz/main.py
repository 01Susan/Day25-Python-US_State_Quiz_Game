import turtle
from readingcsv import ProcessData

screen = turtle.Screen()
screen.title("U.S State Quiz")
image = "blank_states_img.gif"
# Adding a new shape. So that we can add image to our screen
screen.addshape(image)
turtle.shape(image)
data_process = ProcessData()
guess_state = []
# TODO 1. Asking the user for state name


while len(guess_state) != 50:
    answer_state = screen.textinput(title=f"{len(guess_state)}/50 State Correct",
                                    prompt="What's another state name?").title()

    if answer_state == "Exit" or answer_state == "exit":
        data_process.unable_guess(guess_state)
        break
    data_process.check_answer(answer_state, guess_state)

screen.exitonclick()
