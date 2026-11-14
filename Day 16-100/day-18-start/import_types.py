# type 1
import prettytable
# usage - modulename.function/class
table = prettytable.PrettyTable()

# type 2
from turtle import Turtle, Screen
# usage - use the class/function name directly
tim = Turtle()
tom = Turtle()
terry = Turtle()
my_screen = Screen()

# type 3 - not recommended
from random import *
# usage - use any module components directly
print(choice([1, 2, 3]))

# type 4 - alias
import heroes as h
# usage - use the alias name to fetch module components
print(h.gen())

# install new packages as and when needed through pycharm
