from turtle import Turtle, Screen
import random

my_screen = Screen()

terry = Turtle()
terry.shape("turtle")
terry.color("maroon4")

# Challenge 1: Draw a square
for _ in range(4):
    terry.forward(100)
    terry.right(90)


# Challenge 2 - Draw a dashed line
terry.teleport(y=10)
for i in range(15):
    if i % 2 == 0:
        terry.pd()
    else:
        terry.pu()
    terry.forward(10)


# Challenge 3 - Draw a triangle, square, pentagon,
#               hexagon, heptagon, octagon, nonagon
#               and decagon
terry.teleport(x=0, y=20)
my_screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r,g,b

def draw_shape(num_of_sides, t):
    angle = 360 // num_of_sides
    for _ in range(num_of_sides):
        t.forward(100)
        t.left(angle)

for num_sides in range(3, 11):
    # choose random color
    terry.color(random_color())
    # draw a shape
    draw_shape(num_sides, terry)

# clear screen - before next challenge
my_screen.resetscreen()

# Challenge 4 - Random walk
terry.pensize(10)
terry.speed("fast")
directions = [ terry.forward, terry.backward ]
turns = [ terry.left, terry.right ]

for _ in range(100):
    terry.color(random_color())
    current_direction = random.choice(directions)
    current_direction(50)
    take_turn = random.choice(turns)
    take_turn(90)

# Challenge 4 - Alternate solution
my_screen.resetscreen()
terry.pensize(15)
terry.speed("fastest")
directions = [0, 90, 180, 270]

for _ in range(200):
    terry.color(random_color())
    terry.forward(30)
    terry.setheading(random.choice(directions))

# Challenge 5 - Draw a spirograph
my_screen.resetscreen()
directions = [0, 90, 180, 270]
terry.speed("fastest")
for d in range(0, 361, 5):
    terry.color(random_color())
    terry.setheading(d)
    terry.circle(100)

my_screen.exitonclick()