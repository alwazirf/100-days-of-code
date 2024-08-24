import turtle
import pandas as pd

FONT = ("Courier", 20, "normal")

screen = turtle.Screen()
screen.title("U.S States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("./50_states.csv")
all_states = data.state.to_list()
guessed_state_answer = []

while len(guessed_state_answer) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state_answer)}/50 States Correct", prompt="What's another state's name").title()
    
    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_state_answer:
                missing_state.append(state)
        df = pd.DataFrame(missing_state)
        df.to_csv('states_to_learn.csv')
        break;

    if answer_state in all_states:
        guessed_state_answer.append(answer_state)
        state_data = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())

screen.exitonclick()