import turtle
from turtle import Turtle, Screen
import pandas


screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click_cord(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_cord)
#


data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
all_answer_states = []

while len(all_answer_states) < 50:
    guess = screen.textinput(title=f"{len(all_answer_states)} / 50 states",
                             prompt="What's another state's name?").title()
    if guess == "Exit":
        missing_states = [state for state in all_states if state not in all_answer_states]
    #     missing_states = []
    #     for state in all_states:
    #         if state not in all_answer_states:
    #             missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn")
        break
    if guess in all_states:
        all_answer_states.append(guess)
        turtle = Turtle()
        turtle.hideturtle()
        turtle.penup()
        state = data[data.state == guess]
        new_x = int(state.x)
        new_y = int(state.y)
        turtle.goto(new_x, new_y)
        # turtle.write(state.state.item())
        turtle.write(guess)



#state to learn








# turtle.mainloop()
# screen.exitonclick()