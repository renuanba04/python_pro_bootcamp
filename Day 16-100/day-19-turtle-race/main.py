import random
from turtle import Turtle, Screen
from tkinter import messagebox

is_game_on = False
my_screen = Screen()
my_screen.setup(height=400, width=500)
user_bet = my_screen.textinput(title="Make a bet", prompt="Which turtle would win the race? \
            \n(red,orange,yellow,green,blue or purple)")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

if user_bet and user_bet.lower() in colors:

    for index, color in enumerate(colors):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(color)
        new_turtle.penup()
        y_pos = -70 + (index * 30)
        new_turtle.goto(x=-230, y=y_pos)
        turtles.append(new_turtle)

    is_game_on = True
    while is_game_on:

        for turtle in turtles:

            rand_dist = random.randint(0, 10)
            turtle.forward(rand_dist)

            if turtle.xcor() > 230:
                is_game_on = False
                winner = turtle.pencolor()

                if winner == user_bet.lower():
                    messagebox.showinfo("Announcement", f"You've won! The {winner} turtle won.")
                else:
                    messagebox.showinfo("Announcement", f"You've lost! The {winner} turtle won.")

    my_screen.exitonclick()
else:
    messagebox.showinfo("Info", "Invalid choice")
    my_screen.bye()