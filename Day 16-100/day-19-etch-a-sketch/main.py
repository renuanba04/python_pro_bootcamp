from turtle import Turtle, Screen

timmy = Turtle()
my_screen = Screen()

def move_forwards():
    timmy.forward(10)

def move_backwards():
    timmy.back(10)

def turn_clockwise():
    timmy.right(10)

def turn_anticlockwise():
    timmy.left(10)

def clear_drawing():
    my_screen.resetscreen()

my_screen.listen()
my_screen.onkey(key="w",fun=move_forwards)
my_screen.onkey(key="s",fun=move_backwards)
my_screen.onkey(key="d", fun=turn_clockwise)
my_screen.onkey(key="a", fun=turn_anticlockwise)
my_screen.onkey(key="c", fun=clear_drawing)
my_screen.exitonclick()
