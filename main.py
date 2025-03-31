import tkinter.messagebox
import turtle
from turtle import Turtle
import pandas
from tkinter import *

ALIGN = "left"
FONT = ("Comic Sans MS", 12, "normal")

# screen instantiation
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# dataframes
states_df = pandas.read_csv("50_states.csv")
# correct answers
states_correct = []
# tkinter alert boxes

writer = turtle.Turtle()
writer.hideturtle()
writer.color("black")
writer.penup()
answer = ""

while len(states_correct) != 50:
    answer = turtle.textinput(f"{len(states_correct)} / 50 States", "Name Next State: ")
    if answer is None:
        break
    if states_df[states_df.state == answer.title()].empty:
        tkinter.messagebox.showinfo("Invalid Answer", "That is not a State.")
    elif answer in states_correct:
        tkinter.messagebox.showinfo("Answer Already Submitted", "You've Already Submitted This Answer")
    else:
        states_correct.append(answer)
        xcor = states_df[states_df.state == answer.title()].x.values[0]
        ycor = states_df[states_df.state == answer.title()].y.values[0]
        writer.goto(xcor, ycor)
        writer.pendown()
        writer.write(answer.title(), FONT, ALIGN)
        writer.penup()


tkinter.messagebox.showinfo("Number Correct", f"You Got {len(states_correct)} out of 50.  Your correct states are printed for later as csv.")
correct_states_dict = {"states":states_correct}
correct_states_df = pandas.DataFrame(correct_states_dict)
correct_states_df.to_csv("correct_states.csv")

states_list = states_df.state.to_list()
states_to_study = [state for state in states_list if state not in states_correct] #list comprehension
states_to_study_dict = {"States to Study": states_to_study}
study_states_df = pandas.DataFrame(states_to_study_dict)
study_states_df.to_csv("states_to_study.csv")


turtle.mainloop()
