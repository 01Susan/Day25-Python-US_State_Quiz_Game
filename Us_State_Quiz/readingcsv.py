import pandas as pd
from turtle import Turtle


# TODO 2. Reading the CSV file and excessing the series from the Dataframe
class ProcessData:

    def __init__(self):
        self.data = pd.read_csv("50_states.csv")
        self.state_name_list = self.data["state"].to_list()

    def check_answer(self, user_answer, guess_state):
        if user_answer in self.state_name_list:
            t = Turtle()
            t.hideturtle()
            t.penup()
            if user_answer not in guess_state:
                guess_state.append(user_answer)
            # TODO 3 Extracting  x and y value of particular state
            row_value = self.data[self.data["state"] == user_answer]
            # ^|Gives a whole row value of user_answer state
            t.goto(int(row_value.x), int(row_value.y))
            t.write(row_value.state.item())

    # List of states which were unable to guess by user
    def unable_guess(self, guess_state):
        missing_state = []
        for state in self.data.state:
            if state not in guess_state:
                missing_state.append(state)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("missing_state_to_learn")


