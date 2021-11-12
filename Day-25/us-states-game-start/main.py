print("Hello")
import turtle

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
import pandas

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)} out of 50 Correct ", prompt="What another state's name?").title()
    print(answer_state)
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        print(state_data)
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
    elif answer_state.lower() == "exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        print(all_states)
        break


