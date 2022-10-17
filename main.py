import pandas
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"

screen.addshape(image)  # adding a shape to turtle
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
print(all_states)



answer_state = screen.textinput(title="Guess the state", prompt="What's another state?")

#if ans is one of the states:
if answer_state in all_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state] #pulls out the row for that particular state that the user guessed right
    t.goto(x=, y=)
    #if they got it right:

        #create a turle to write the name on the map






screen.exitonclick()
